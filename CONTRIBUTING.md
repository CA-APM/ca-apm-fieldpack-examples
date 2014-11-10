# Contributing to CA APM

We are glad you want to contribute to CA APM!

## Contribution Process

We have a simple process that utilizes the [GitHub](https://guides.github.com/introduction/flow/index.html) and **Github Issues**:

1. Sign or be added to an existing [Contributor License Agreement (CLA)](https://communities.ca.com/become-a-contributor).
1. Sign up or login to your [GitHub account](https://github.com/signup/free)
1. Fork the repository on GitHub
1. Report an issue or make a feature request [here](#issues).
1. Add features or fix bugs
1. Create a [Github Pull Request](http://help.github.com/send-pull-requests/)
1. Do [Code Review](#cr) with the **CA APM Engineering Team** or **CA APM Core Committers** on the pull request.

### <a name="pulls"></a> CA APM Pull Requests

CA APM is enterprise grade software. We strive to ensure high quality throughout the CA APM experience. In order to ensure this, we require a couple of things for all pull requests to CA APM:

**Tests:** To ensure high quality code and protect against future regressions, we require all the
  code in CA APM to have at least unit test coverage. See the [spec/unit](https://communities.ca.com/testing)

In addition to this it would be nice to include the description of the problem you are solving
  with your change. You can use [CA APM Issue Template](#issuetemplate) in the description section
  of the pull request.

### <a name="cr"></a> CA APM Code Review Process

The CA APM Code Review process happens on Github pull requests. See
  [this article](https://help.github.com/articles/using-pull-requests) if you're not
  familiar with Github Pull Requests.

Once you create a pull request, the **CA APM Engineering Team** or **CA APM Core Committers** will review your code and respond to you with any feedback they might have. The process at this point is as follows:

1. 2 thumbs-ups are required from the **CA APM Engineering Team** or **CA APM Core Committers** for all merges.
1. When ready, your pull request will be tagged with label `Ready For Merge`.
1. Your patch will be merged into `master` including necessary documentation updates
  and you will be included in `CHANGELOG.md`. Our goal is to have patches merged in 4 weeks
  after they are marked to be merged.

### <a name="oh"></a> Developer Office Hours

We hold regular "office hours" on CA Communities that you can join to review contributions together,
ask questions about contributing, or just hang out with CA APM Software employees.  The regularly scheduled CA APM hangouts occur on Mondays and Wednesdays at 3pm Eastern / Noon Pacific.

### Contributor License Agreement (CLA)
Licensing is very important to open source projects. It helps ensure the
  software continues to be available under the terms that the author desired.

Depending on the needs of the project, CA APM uses one of two possible licenses.  Each project should have the appropriate license specified in the `LICENSE.md` file. One option is to use the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0.html).  This license does not require that work be contributed back to the community.  Another option is to use the [Eclipse 1.0 license](https://www.eclipse.org/legal/epl-v10.html) to strike a balance between open contribution and allowing you to use the software as you wish.

The license tells you what rights you have that are provided by the copyright holder.
  It is important that the contributor fully understands what rights they are
  licensing and agrees to them. Sometimes the copyright holder isn't the contributor,
  most often when the contributor is doing work for a company.

To make a good faith effort to ensure these criteria are met, CA APM requires an Contributor License Agreement (CLA)
  for contributions. This agreement helps ensure you are aware of the
  terms of the license you are contributing your copyrighted works under, which helps to
  prevent the inclusion of works in the projects that the contributor does not hold the rights
  to share.

It only takes a few minutes to complete a CLA.

You can complete our:
  [CLA online at https://www.clahub.com/agreements/CA-APM/<repo_name>](https://www.clahub.com/agreements/CA-APM/<repo_name>) (link will vary with each project).
  
### CA APM Obvious Fix Policy

Small contributions such as fixing spelling errors, where the content is small enough
  to not be considered intellectual property, can be submitted by a contributor as a patch,
  without a CLA.

As a rule of thumb, changes are obvious fixes if they do not introduce any new functionality
  or creative thinking. As long as the change does not affect functionality, some likely
  examples include the following:

* Spelling / grammar fixes
* Typo correction, white space and formatting changes
* Comment clean up
* Bug fixes that change default return values or error codes stored in constants
* Adding logging messages or debugging output
* Changes to ‘metadata’ files like Gemfile, .gitignore, build scripts, etc.
* Moving source files from one directory or package to another

**Whenever you invoke the “obvious fix” rule, please say so in your commit message:**

```
------------------------------------------------------------------------
commit 360acb3f82d55d762b0cf9c1d1e99b144a8ed3b5
Author: klinebch <klinebch@foo.com>
Date:   Fri Oct 10 11:30:11 2014 -0500

  Fix typo in help text.

  Obvious fix.

------------------------------------------------------------------------
```

## <a name="issues"></a> CA APM Issue Tracking

CA APM Issue Tracking is handled using Github Issues.

Issues include both problems and feature requests.  Issues should be filed under the project to which they correspond.  Each project has a Issues link on Github on the right-side nav menu.  You can also go directly to the issues pages by visiting `http://github.com/ca-apm/<repo name>/issues`.

In order to decrease the back and forth an issues and help us get to the bottom of them quickly
  we use below issue template. You can copy paste this code into the issue you are opening and
  edit it accordingly.

<a name="issuetemplate"></a>
```
### Version:
[Version of the project installed]

### Environment: [Details about the environment such as the Operating System, cookbook details, etc...]

### Scenario:
[What you are trying to achieve and you can't?]

### Steps to Reproduce:
[If you are filing an issue what are the things we need to do in order to repro your problem?]

### Expected Result:
[What are you expecting to happen as the consequence of above reproduction steps?]

### Actual Result:
[What actually happens after the reproduction steps?]
```

## CA APM Community

CA APM is made possible by a strong community of developers and system administrators. If you have
  any questions or if you would like to get involved in the CA APM community you can check out:

* [CA APM Community](https://communities.ca.com/community/ca-apm).  Core APM community for general discussion 
* [CA APM Dev Community](https://communities.ca.com/community/ca-apm/apm-dev).  Developer community for dev-specific tools and dialog.
