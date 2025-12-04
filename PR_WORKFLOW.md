# Pull Request Workflow Guide

This guide explains how to create a Pull Request (PR) that references GitHub Issues to satisfy the Project Management requirements.

## Creating a PR that References an Issue

### Step 1: Create a Feature Branch

```bash
# Example: Working on Issue #1 - Create hardcoded exercise library
git checkout -b feature/exercise-library
```

### Step 2: Make Your Changes

Work on the feature described in the issue. For example, if working on Issue #1:

```bash
# Edit your files
# Make commits as you go
git add .
git commit -m "Add exercise library data structure

Implements the hardcoded exercise library as described in Issue #1.
Includes 11 exercises with name, duration/reps, and difficulty level.

Relates to #1"
```

### Step 3: Push Your Branch

```bash
git push -u origin feature/exercise-library
```

### Step 4: Create the Pull Request


1. Go to your repository on GitHub
2. Click "Pull requests" tab
3. Click "New pull request"
4. Select your feature branch
5. Add a title and description that references the issue

**Important: Use keywords to link the PR to issues:**

Use these keywords in your PR description to automatically link and close issues:
- `Closes #1`
- `Fixes #1`
- `Resolves #1`

Example PR description [only if you have created a template - do not type this structure every time!!]:
```markdown
## Summary
Implements the hardcoded exercise library with 11 fundamental exercises.

## Changes
- Created exercise data structure in `src/workout_builder.py`
- Each exercise includes name, duration/reps, and difficulty level
- Exercises stored in dictionary format for easy access

## Testing
- Manually verified all exercises have required fields
- Tested exercise retrieval in workout routines

## Closes
Closes #1

## Checklist
- [x] Code follows project style guidelines
- [x] All exercises have required fields
- [x] Data structure is accessible by other components
```


## Tips for Good PRs

1. **Reference Issues**: Always mention the issue number in your PR
2. **Clear Description**: Explain what changed and why
3. **Test Evidence**: Show that your code works
4. **Small PRs**: Keep PRs focused on one issue/feature
5. **Request Reviews**: Get feedback from teammates


## Meeting the Requirements

To earn full points for Project Management (25 pts):

1. ✓ **5-8 Issues created with owners and due dates (10 pts)**
   - Created 8 issues in `github-issues.json`
   - Each has `assignee` and `due_date` fields
   - Upload these to GitHub

2. **One PR open or merged that references at least one Issue (10 pts)**
   - Follow the workflow above
   - Create a feature branch
   - Make changes
   - Create PR with "Closes #X" in description

3. ✓ **Link to Team Prompt Library added to README (5 pts)**
   - Already added to README.md
   - Create the wiki page and update the link

## Next Steps

1. Replace placeholder team member names with actual GitHub handles
2. Upload issues to GitHub
3. Create your first PR following this workflow
4. Set up your Team Prompt Library wiki page
