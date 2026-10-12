# Contributing

Submit an original creator post, not an unattributed repost. Include the creator profile, public video URL, a short descriptive title, and the author's exact evidence for the tool or workflow. Do not turn a task description into a prompt or infer tool use from a visual style.

The collection has four attribution groups: author-declared Claude Motion, mixed workflows including Claude Motion, recorded generated artifacts, and related references with unconfirmed Claude Motion use.

Updates are manual. A maintainer reviews attribution and content, prepares full-length MP4 viewing copies plus a poster and preview, and uploads them to the configured public R2 bucket with content-hashed object names and immutable cache headers. Verify the uploads before linking them publicly. Keep source downloads, credentials and upload receipts outside this repository.

Update `data/videos.json` and `data/changelog.json`, then run:

```bash
python3 scripts/build_readme.py
```

Check both README files and the generated case pages before committing. Only maintainers with explicit publishing authorization should push or change hosted objects. For an attribution correction or removal, use the correction issue form.
