# Disclaimer

By contributing you accept to provide code that comply to the following code rules. Any pull request may be stalled until fixed.
It's important for everyone, be it contributors or reviewers, to have a clear compile log so they can easily spot and fix new arising problems / warning.

# Code contribution rules

* Indent your code. Using automatic indentation is recommended, at least for new apps
* Test and take in account the return code each time it's needed
* Have an error management in your app
* Make reusable content (class, structs, gui filler functions, ...)
* Document global processing as well as tricky parts, don't be lazy, some may contribute to your own contribution. Information inside the code is really appreciated
* Fix your compilation warnings before making a pull request. ALL your warnings. It's making a terrible noise in the compilation log each time we accept PRs with warnings everywhere
* Provide access to your sources via a public repository
* **!! NEVER USE std::rand or std::srand, they are known to break to heap/stack/memory !!**

# AI code
We love and welcome AI code, as long as:
- It didn’t violate the TOS of the AI provider and AI model.
- It doesn't substantially resemble or duplicate open-source code with licensing incompatible to this project's licenses.
- You reviewed the code.
- You understood the code.
- You tested the code.
- **You checked that AI code IS NOT using std::rand or std::srand !**
# A note on Pull Requests

* PRs should be up to date with 'next'
* Each new functionality should have it's own PR, don't put too much files/commits into a single PR. When it's too much commits, one can make a new branch and report only the modified files in a single commit, to make the review easier
* Merging of any PR is up to the maintainers good will

# naming and usage rule
* Use English
* `var_and_func_example` (snake_case)
* `_private_member_of_class_example` (_snake_case) (not yet covered all in codebase but new apps. You are welcomed to correct them.)
* `namespaceexample`
* `ClassNameExample` (CamelCase)
* `objectNameExample` (camelCase)
* `func_arg_ex` (snake_case and abbreviation is allowed in small scope functions)
* Don’t use `typedef` keyword in C++ code  
* `goto` is not allowed

# which license of code is safe to use   
 - MIT: It's safe to copy MIT license, as long as you keep original copyright info.   
 - MPL: It's safe to copy MPL license, as long as you follow Mozilla's agreement.
 - GNU (GPL 2/3 / AGPL): This project is under GPL which means it's safe to use GPL code here as long as you open source your the distro under GPL license.  
 - The Unlicensed: safe to use.
 - BSD: safe to use.
 - WTFPL: Safe to use.  
 - CC0: safe to use.
