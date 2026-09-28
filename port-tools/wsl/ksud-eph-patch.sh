#!/bin/sh
set -u
cd /root/KernelSU-dm3q
python3 - <<'EOF'
p = 'userspace/ksud/src/cli.rs'
t = open(p).read()
old = """        /// manager package name
        #[arg(long, default_value_t = String::from("me.weishu.kernelsu"))]
        package_name: String,
    },"""
new = """        /// manager package name
        #[arg(long, default_value_t = String::from("me.weishu.kernelsu"))]
        package_name: String,

        /// Ephemeral temp-root use: skip replacing an existing /data/adb/ksud
        #[arg(long)]
        ephemeral: bool,
    },"""
assert old in t
t = t.replace(old, new)
old2 = """        Commands::LateLoad {
            magica,
            allow_shell,
            post_magica,
            kmi,
            package_name,
        } => {"""
new2 = """        Commands::LateLoad {
            magica,
            allow_shell,
            post_magica,
            kmi,
            package_name,
            ephemeral,
        } => {"""
assert old2 in t
t = t.replace(old2, new2)
old3 = "            let result = crate::late_load::run(&package_name, kmi, allow_shell);"
new3 = "            let result = crate::late_load::run(&package_name, kmi, allow_shell, ephemeral);"
assert old3 in t
t = t.replace(old3, new3)
open(p, 'w').write(t)
print('cli.rs patched')
EOF
python3 - <<'EOF'
p = 'userspace/ksud/src/late_load.rs'
t = open(p).read()
old = "pub fn run(_package_name: &String, kmi: Option<String>, allow_shell: bool) -> Result<()> {"
new = "pub fn run(\n    _package_name: &String,\n    kmi: Option<String>,\n    allow_shell: bool,\n    ephemeral: bool,\n) -> Result<()> {"
assert old in t
t = t.replace(old, new)
old2 = "    utils::finish_install(None).context(\"Failed to finish ksud installation\")?;"
new2 = """    if ephemeral {
        info!("ephemeral mode: skipping ksud installation (temp root, this boot only)");
    } else {
        utils::finish_install(None).context("Failed to finish ksud installation")?;
    }"""
assert old2 in t
t = t.replace(old2, new2)
open(p, 'w').write(t)
print('late_load.rs patched')
EOF
