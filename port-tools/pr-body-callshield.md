Implements issue #22: an "Answer & hang up blocked calls" toggle so spam can't leave voicemail, per the approved shape in that thread.

## Behavior (as approved)

- **Off by default**, hard-block verdicts only (`shouldSilence` paths — Silent Voicemail, low-confidence auto-mute, category voicemail, direct-boot — are untouched).
- **ANSWER_PHONE_CALLS is requested only when the toggle is enabled** (Settings launcher), never during onboarding. With the setting off, behavior is identical to upstream.
- Plain rejection stays the fallback everywhere: missing permission, busy state, or any error takes the normal block response. Never fails open.
- Screening response is sent first; the process-wide `AnswerHangUpController` arms only for that number (atomic, refuses while another call is mid-answer/hang-up).
- Safety rules from the issue: active call never touched (normal reject), outgoing call cancels pending hang-up, call-end/second-ring aborts, audio-only answering, numbered PHONE_STATE copy only.
- Trust loophole closed: auto-answered calls leave short INCOMING rows, so answered-caller trust and repeated-urgent ignore INCOMING rows under 15 s while the setting is on (missed calls still count; both queries unchanged with the setting off).
- Settings text lists the trade-offs: autodialers may redial a live number; some carriers need a longer delay (1–10 s stepper); screen may light up briefly; `acceptRingingCall`/`endCall` act on the foreground call (deprecated since API 29, same as SpamBlocker).
- New values in backup/restore (`answer_hang_up_mode`, `hang_up_delay_seconds`, clamped 1–10, default 1).

## Validation

- Full unit suite green: **1355 tests, 0 failures** (JDK 21 run; `-PbenchHeadroom=3` on this host per the suite's own slow-host escape hatch).
- `ktlintCheck`, `detekt`, `lintRelease` all pass.
- New tests: controller state machine, decision logic, backup/restore of the new settings, trust queries, onboarding-permission gating.
- Device-tested per the issue (emulator end-to-end + Galaxy S23 Ultra daily use); branch merged up to current `origin/master` (cert-pin and lockfile refreshes included).

Closes #22.
