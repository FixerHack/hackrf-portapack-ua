# Trusted contributors

Some proof requirements from the [Pull Request template](https://github.com/portapack-mayhem/mayhem-firmware/blob/next/.github/pull_request_template.md) may be waived for contributors who have built a track record of producing working, tested, and properly documented changes. This page defines what "trusted contributor" means, what can be waived, and how the status is granted or revoked.

## Why this exists

Requiring full proof on every PR (compile logs, real-device screenshots, RF captures, wiki updates) is the right default. It keeps the firmware stable and prevents untested code from reaching users. But for contributors who have repeatedly shown they hold themselves to that standard, asking for the same evidence on every small refactor or bugfix becomes friction rather than quality control.

This exception exists to reduce that friction **without lowering the bar for the firmware itself**.

## Who qualifies

There is no automatic threshold. Trusted-contributor status is granted at maintainer discretion, typically after a contributor has:

- Merged **at least 3 PRs** that included full proof (compile, real-device, and RF evidence where applicable)
- Created or properly updated the corresponding **wiki pages** for each of those PRs
- Responded constructively to review feedback
- Not shipped a PR that was later reverted or hot-fixed due to missing testing

Maintainers may also grant the status to long-standing project members, core maintainers of related projects, or contributors with a verifiable history elsewhere.

If you believe you qualify and the status would be useful for your upcoming work, you may open a discussion or mention it in your next PR, but please do not assume the status applies until a maintainer confirms it.

## What can be waived

The proof sections on a PR fall into three tiers:

| Section | Waivable? | Notes |
|---|---|---|
| 🖥️ Proof it compiles | ✅ Yes | Maintainers can re-run the build themselves. |
| 📱 Proof of testing on a real device | ⚠️ Sometimes | Waivable for changes that don't affect runtime behaviour (refactors, comment fixes, build-system tweaks). Not waivable for UI, app logic, or hardware-interacting changes. |
| 📡 Proof against a real emitter/receiver | ❌ **Never waivable** | Maintainers cannot physically re-verify RF behaviour against arbitrary hardware. This proof is required from everyone, every time, without exception. |
| 📚 Wiki documentation | ❌ **Never waivable** | If the PR adds or modifies a user-facing app, the wiki must be kept in sync. |

When a section is waived, the contributor should still mark the section in the PR as:

> N/A - trusted contributor *(short reason, e.g. "internal refactor, no user-visible change")*

This leaves an audit trail that makes the review history easier to follow.

## Scope of a waiver

A waiver applies **per PR**, not per contributor. Even a trusted contributor should provide full proof when:

- The change touches RF, TX/RX, or protocol code (see the table above)
- The change is large, architectural, or risky
- The change affects an app they have not previously worked on
- A maintainer explicitly requests proof for that PR

When in doubt, include the proof anyway. Trusted-contributor status is a courtesy to save time on trivial changes, not a blanket exemption.

## How status is revoked

Trusted-contributor status can be revoked at maintainer discretion if:

- A PR merged under the waiver is found to be broken, untested, or missing its wiki update
- The contributor repeatedly skips proof on changes where it was warranted
- The contributor becomes inactive for an extended period (status may be re-granted on return)

Revocation is not a punishment, it simply restores the default expectation of full proof on every PR. Re-earning the status follows the same path as earning it the first time.

## For maintainers

When reviewing a PR from a trusted contributor:

- Confirm the N/A reasoning is accurate for the scope of the change
- Check that the RF proof and wiki update (where applicable) are still present, these are never waived
- If something feels off, ask for the proof anyway; the waiver is a default, not a guarantee
- Record revocations in the project discussions or a dedicated issue so other maintainers are aware

---

*If you have questions about this policy, open a discussion on the repository rather than asking in individual PRs.*