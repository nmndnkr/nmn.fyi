# DataSelf — Product Case Study

## Product thesis

Your AI learns how you work. You should be able to take that with you.

DataSelf turns real LLM sessions into a local, portable memory of workflows,
trust boundaries, delegation patterns, and decision rules—without saving the
conversation itself.

## The product turn

The hackathon version counted prompts, responses, copies, and corrections. That
made activity visible, but activity was not the thing worth carrying between
providers.

The durable value was behavioral: how someone researches, what they verify, what
they delegate, and what “done” means to them. Provider history can remember that,
but the user cannot take it elsewhere.

**Product insight:** The useful unit is not a prompt. It is a reusable working
rule.

## First user and job

**First user:** An individual whose work with an LLM improves as the model learns
how they operate.

**Job to be done:** When I change LLMs, help me bring how I work so I do not have
to teach the new one from zero.

Teams were deliberately excluded. Permissions, shared truth, and governance
widen the system before the core transfer is proven.

## Product decisions

| Chose | Over | Why | Accepted cost |
|---|---|---|---|
| Behavioral rules | Raw transcripts or embeddings | Portable and legible without retaining the most sensitive material | Less conversational nuance |
| Active LLM extraction | Sending the chat to a second model | The provider already has the session, so extraction needs no second copy | Adapter quality depends on provider UI |
| Local Markdown | Cloud storage and accounts | The user can inspect, edit, move, or delete every memory | No automatic multi-device sync |
| Automatic provisional updates | Approving every item after every session | A menu-bar tool cannot become another inbox; edits remain reversible | Weak inferences can appear temporarily |
| One portable context file | Provider-specific connectors | Markdown works everywhere and made transfer testable in one week | The first migration step is manual |

### Explicit non-goals

- No cloud sync.
- No team memory.
- No raw chat archive.
- No claims about what providers train on.
- No universal browsing surveillance.

## MVP loop

1. **Start:** Toggle recording from the macOS menu bar.
2. **Work:** Use the active LLM normally; retain only content-free events.
3. **Extract:** Ask the active LLM for a strict memory patch at session end.
4. **Validate:** Reject unknown types, multiline content, or mismatched evidence.
5. **Move:** Export `dataself-context.md` and bring it to a new LLM.

The local Markdown graph is the source of truth. New memories begin as
provisional, strengthen with repeated real-session evidence, and remain
inspectable, editable, and deletable.

## How I tested it

Two fresh anonymous ChatGPT sessions received the same vague new-product
request.

**Without DataSelf:** The model selected a product direction, proposed a broad
multi-week build, and asked several questions at once.

**With DataSelf:** The model made no product assumption, asked one focused
question, kept the MVP narrow, and reserved technical execution until direction
was clear.

**Result:** Four of five known working behaviors transferred without a corrective
message. The fifth—three-line completion handoff—was not exercised because the
test stopped at product definition.

The implementation also passes 19 automated tests covering the privacy ledger,
strict memory-patch validation, evidence links, graph updates, context export,
and provider normalization.

## Success metrics

**North star:** Real sessions migrated with materially less workflow
re-explanation.

| Metric | Target | Current evidence |
|---|---:|---|
| Known preferences followed after migration | At least 4 of 5 | Passed: 4/5 |
| Raw conversation retained | 0 bytes | Passed |
| Memories linked to real sessions | 100% | Passed |
| Invalid patches written | 0 | Passed in automated tests |
| Setup to first memory update | Under 10 minutes | Unproven |
| Corrective workflow messages | Fewer than baseline | Needs multi-session test |

Prompt volume is intentionally not the north star. It would reward usage rather
than continuity.

## What is proven—and what is not

The prototype proves that behavioral memory can transfer. It does not yet prove
that enough people feel the reset, trust automatic extraction, or keep using the
system.

### Next experiment

Recruit five heavy LLM users for three sessions each. Measure:

- setup time;
- memory edit and deletion rate;
- corrective messages with and without context;
- whether users choose to migrate the file again.

### Risks to watch

- Provider UI changes breaking automatic capture.
- Confident but wrong memories becoming sticky.
- A context file growing until it becomes noise.
- Users valuing convenience more than portability.

## Links

- [Product case study](https://nmn.fyi/work/dataself/)
- [GitHub repository](https://github.com/nmndnkr/dataself)
- [Live product page](https://nmndnkr.github.io/dataself/)
- [Two-page PDF](output/pdf/DataSelf-Product-Case-Study.pdf)
