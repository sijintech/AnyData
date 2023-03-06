# AnyData

General purpose data science SDK for non-programmers.

## Roadmap

- Phase 1: collect best practices, examples
- Phase 2: refactor the best practices into useful functions
- Phase 3: add cli, automation, etc to make the user experience complete

For now we are in the Phase 1.

## Pain point

Many data scientists (broad concept, any one who needs to process datasets) program just like engineers, who care only if the code finish its task. Thus, several problems arises:
1. code versioning problem. Due to the lack of proper training in programming, many of the data scientist never use git to track their codes.
2. poor documentation, thus others couldn't understand your code, or even yourself won't be able to understand it after several months.
3. poor reusability. Many data scientists just copy and paste functions or even just code snippet from old project into a new project when they find some tasks that he/she has performed before.
4. poor reproducibility. Many data scientist are using R, Stata, or Jupyter notebook interactively to process the data, which makes their script hard to reproduce because there is a variable of execution sequence not recorded by the script.

## Targeting audience

social scientist, business school researshers

## Featuring (future)

1. a cli tool to help you initialize your project
2. a customizable anydata python package containing common data science functions
3. experience and procedures for large dataset (>1T)
