---
layout: post
title: "Checklist for creating an R package"
date: 2021-09-21 21:00:00 -0000
categories: R
tags: checklist
---

I started writing R packages in early 2017. For a while I found the initial set up for a new package involved more guess-work than I'd like (e.g. start from GitHub first or RStudio? When do you normally add a license?).
Here's my personal checklist for getting a minimal R package started in a consistent way:

1. Create an empty GitHub repo (with a license)
1. Create a new project in RStudio (tick the box to create a git repo)
1. git rm the default hello world function
1. [Add a git remote](https://docs.github.com/en/get-started/getting-started-with-git/managing-remote-repositories)
1. [Cache git credentials](https://happygitwithr.com/credential-caching.html)
1. [Add username and email to git](https://happygitwithr.com/hello-git.html)
1. stage, commit, and push (may need a personal access token if GitHub is set up with 2FA)

This checklist reflects how I currently work. So it'll most likely change as my workflow evolves.

## Bonus Checklist
Some extras to make life easier for others (including future self):

- Update the [DESCRIPTION file](https://r-pkgs.org/description.html)
- Add some basic documention:
  - Create a README with usethis::use_readme_rmd()
  - Add a [status badge](https://www.repostatus.org/)
  - Add a URL to the GitHub repo webpage
- Maybe [set up CI](https://juliasilge.com/blog/beginners-guide-to-travis/) and a [pkgdown site](https://pkgdown.r-lib.org/) for larger projects

This book is an excellent resource for taking best practice further: [rOpenSci Packages: Development, Maintenance, and Peer Review](https://devguide.ropensci.org/).
