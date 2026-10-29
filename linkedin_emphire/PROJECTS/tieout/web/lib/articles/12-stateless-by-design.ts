const body = `
## The site is a viewer, and viewers can be stateless

This site deploys to Vercel as one project with two services: a static export of the Next.js frontend, and the FastAPI app as a single Python function. The rewrites are two lines in the repository: /api/* goes to the function with the path preserved, everything else serves from the static files. No environment variables. No database. No queue.

The reason that works is that the site was never meant to own state. The evidence is the bundle, and the bundle is a file in a git repository, versioned, committed, and re-derivable. The site is a viewer for those files: it lists runs, renders bundles, runs verify on request, and diffs two runs. A viewer's state is the repository.

## The one stateful habit, handled explicitly

There is exactly one place the app wants to write: the verify endpoint, which by local convention drops a verify_report.json next to the bundle it just checked. On a serverless function the filesystem is ephemeral, and the write may not survive the request. So the write is best-effort by design: the report is always returned in full in the HTTP response, which is what the UI consumes, and the file write is a courtesy for local and container deployments where the runs directory is real. A test in the repository simulates the read-only filesystem and asserts the response stays complete. The site does not pretend to persist what the platform does not.

## The dependency story, pinned

The function installs its dependencies with uv sync --locked against a committed uv.lock, on the Python version the platform actually ships (pinned by .python-version). And because the platform installs the app as a wheel into the function's venv, the entry point passes the deployment root explicitly, so runs/ and docs/ resolve against the deployed tree, not against an installed package's file location. Each of these is a small, testable decision, and together they are the difference between a deploy that works on day one and a deploy that works after three support tickets.

## Cold starts, stated plainly

The static pages are files: they load with no function involved, at any time. The API function cold-starts after idle, adding a second or two to the first request after roughly fifteen quiet minutes. For a site whose content is a handful of bundles and four pages of docs, that is the entire cost of the hosting. The evidence does not live on the function, so there is nothing to lose when the function sleeps.
`;

export { body };
