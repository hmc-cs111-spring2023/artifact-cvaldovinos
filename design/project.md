# Project proposal

## The user and a language

This section describes who the project would serve and why a language might be a
good way to meet their needs.

### What's the need?

_What need is met by your idea? Who are you helping? What is that person's
experience like now? What would their experience be like if you could help
them?_

I am helping economists (both professionals and students) to be able to perform financial calculations without having to perform them manually, pay for expensive software, use an Google/Excel sheet for just one line, or look for an X formula calculator and use some weird website. With my DSL implementation, their experience could be improved as they could just type one line of code to perform the calculation as they would have in a Google/Excel sheet.

### Why a language?

_Why is a DSL appropriate for your user(s)? How does it address the need?_

A DSL is appropriate for the users because it addresses these economists' need to perform calculations without having to open a Google/Excel sheet and have random sheets stored with a few lines of work. Since these users are already having to perform these calculations with some version of typing, whether it be on an online or handheld calculator, they will be able to type a format which follows the conventions of economic formulas and software to input calculations. This means they already have a sufficient technical background with putting variables into a formula so they will not require any more background than is already expected to be able to perform such calculations.

### Why you?

_What excites you about this idea? How did you come up with it?_

I came up with this idea because I was in my Economics class and I was recalling how bothersome it has been in the past to have to find different calculator tools or open up a Google sheet just for one or two calculations for prior Economics assignments. While I may not have to use these tools in the future, I can appreciate how useful they may be for others in my position who want to just quickly perform a couple calculations for a homework set without having to open a google sheet and then find google sheets documentation on what order the arguments go into the formula. Additionally, I am excited to be able to apply my background in Computer Science to create a tool for people studying another field.

### Domain

_Describe the project's domain in five words._

Economic and Finance Formula Calculations

### Interface (syntax)

_How might the user interact with the language? What does programming look
like? Why is this the right way to interact with the problem domain?_

A user would interact with this language in a similar format to what is the standard of Google/Excel sheets, which is like calling functions with multiple arguments in general purpose programming languages (i.e formula(arg1, arg2, ...) ). This is the right way to interact with the problem domain because many of the users are likely not coming from programming backgrounds, or at least this is not an expected requisite, so in asking them to write code, I am hoping to keep their experience as similar to that which they are used to in used the existing software, avoiding many of the technical concepts we use as programmers.

### Operation (semantics)

_What might happen when a program runs? How does a program interact with the
user? What kinds of errors might occur, and how might they be communicated to
the user?_

When a program runs, it will check for function calls and their respective arguments, telling users if they have provided invalid arguments (i.e. argument which must be positive was given a negative value, 2 arguments given when 1 was expected, etc.) This would also be useful for users because in my experience, the error handling by software like Google and Excel is minimal and not very useful for determining what was wrong with the input. This will require more testing to ensure that the errors provided are more clear for the users who are not expected to have backgrounds in coding. Some examples of error handling I have considered before are: "division by zero error", "Invalid value for X", and "Not enough arguments. This function expects the following arguments: X, Y, and Z".

### Expressiveness

_What should be easy to do in this language? What should be possible, but
difficult? What should be impossible or very difficult?_

It should be easy to store quantities and perform basic Economics formulas in google sheets such as: SUM() and VARIANCE(). This also means it should be possible to perform basic arithmetic operations (+, -, *, /) with the outputs of these formulas. People should be limited in what they can express to the scope of these operations and formulas from Google/Excel so that they are not confused when they combine different operations and see unclear behavior as they would not have the technical background to know how to resolve it or even recognize it as a bug at times.

I am not fully certain of which finance formulas I want to implement, since I know I will have to limit them as there are many but I want to prioritize some of the most used ones such as: PV(), FV(), and NPV(). This will be an ongoing decision and depending on how much language design will go into each formula, I may do more or less to ensure I am not spending too much time per task relative to the functionality being gained.

### Related work

_Are there any other DSLs in this domain? If not, describe how you know there
aren't and conjecture why not. If so, describe them and provide links. How well
do they address the need? Are there any particularly admirable qualities of the
language? Are there parts of the language you think could be improved?_

In researching other DSLs in this domain, I found it interesting to find that some people already consider Excel to a be a finance Domain Specific Language: https://medium.grid.is/excel-a-domain-specific-language-for-finance-e9ff6e6e3972#:~:text=Excel%20is%20indeed%20a%20Domain,darn%20good%20one%20at%20that. While I had not considered this, it does seem to be fulfill the definition of a DSL, being confined to a particular problem/domain and users do write in it to communicate with the computer which returns desired outputs. However, as I have discussed above, I am looking to improve upon this experience, though i will be lacking the useful UI it has. Additionally, I found that the python library numpy does contain some of the operations I want to implement: https://pythontic.com/finance/cashflow-modeling. Based off the documentation I looked over, it does look like it can be used to produce very readable code. There are some minor differences between the experience of using this library and my experience using Google sheets, including function names which I would like to maintain consistent but it seems generally similar to the goal I am aiming for with my DSL implementation.

## The Project

This section examines whether the idea makes for a good CS 111 project.

### Suitability

_If someone were to work on this project, what percentage of their time would be
spent directly engaging in the **language** aspects of this project (e.g.,
making language design decisions), as opposed to "systems" aspects of the
project (e.g., implementing a complicated semantics that doesn't require a lot
of language design)?_

Though I am seeking to maintain syntax from Google and Excel, I would like to test out new design implementations which can be challenging so I think this project will require about equal parts time complexity on the language designs I am hoping to test (50%) as on the "systems" aspect and implementation (50%). If I do find that trying to create new designs demands too much implementation complexity, I will reduce the design structures I am planning to work on and I will explain the technical difficulties which prevented me from being able to design the DSL in the fashion I desired so that I do not spend a disproportionate amount of time implementing my designs but I cna still convey my concepts.

### Scope

_How big an idea is this? How ambitious is this project?_

I think this project is not too ambitious for the remainder of the semester that we have to work on it. However, it is a very big idea and I think that based on the experience with the PicoBot DSL experiment, I may encounter roadblocks which I am accounting for because while I would like to test out new designs, my primary goal would be to get the functionality of Excel and Google sheets so that I can address the needs I outlined of users.

More clearly, I would like to: Meet the needs of users and allows for performing calculations in a manner which does not require a much different background than being able to use Excel/Google Sheets. Then getting into the challenges I have set for myself, I would like to build upon this implementation and try out new design decisions, such as allowing for argument inputting to differ from standard practices in Excel/Google Sheets, and handle errors in a more explicit manner than the current ambiguous errors users see.

### Benefits and drawbacks

_Why might this be a good idea for a project? Why might this not be a good idea
project?_

I think this might be a good idea for a project because it has a clear expected outcome and there is room for creativity and exploring different design techniques which we have learned about. It also is for a domain outside of Computer Science though it follows the conventions we are used to in general purpose programming languages of calling functions with arguments. However, it might not be a good idea for a project because if their are difficulties achieving the standard convention used by Excel/Google sheets and you have to go with a different design approach then the resulting tool at the end of this project may be more complex to use than the standard existing ones which could feel disappointing.