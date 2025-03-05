# Report for assignment 4

## Project

Name: Toga

URL: https://github.com/beeware/toga

Toga is a cross platform GUI toolkit. It consists of a library of base components with a shared interface to simplify platform-agnostic GUI development.

#### Architecture: 
![toga_architecture](https://github.com/user-attachments/assets/ccbd3cf1-bbc9-4014-8835-337751a0890e)


## Onboarding experience

Our initial plan was to continue with the same project that we used for the previous assignment. Searching for issues we realized that the project lacks a lot of documentation and that the current issues are either to small or too complex to fix within the scope of this assignment. We therefore decided to look for different repositories and finally selected the Toga repo, because of it's extensive documentation and beginner-friendly usability for contribution. The setup of the project was quite straight-forward and we could easily find issues to work on with the label filtering on github. We finally decided to choose and issue that was both well described and seemed appropriate to work on in the scope of this assignment.

## Effort spent

| Task                           | Amanda (hh:mm) | Herold (hh:mm) | Jannik (hh:mm) | Karin (hh:mm) | Zyad (hh:mm) |
|--------------------------------|---------------|---------------|---------------|--------------|-------------|
| **1. Plenary discussions/meetings** | 00:00 | 00:00 | 00:00 | 00:00 | 03:30 |
| **2. Discussions within subgroups** | 00:00 | 00:00 | 00:00 | 00:00 | 03:30 |
| **3. Reading documentation** | 00:00 | 00:00 | 00:00 | 00:00 | 03:00 |
| **4. Configuration and setup** | 00:00 | 00:00 | 00:00 | 00:00 | 00:30 |
| **5. Analyzing code/output** | 00:00 | 00:00 | 00:00 | 00:00 | 04:00 |
| **6. Writing documentation** | 00:00 | 00:00 | 00:00 | 00:00 | 03:00 |
| **7. Writing code** | 00:00 | 00:00 | 00:00 | 00:00 | 05:00 |
| **8. Running code** | 00:00 | 00:00 | 00:00 | 00:00 | 02:30 |
| **Total** | **00:00** | **00:00** | **00:00** | **00:00** | **24:00** |

## Overview of issue(s) and work done.

### Issue #2144

Title: Configurable text line height in Canvas 

URL: https://github.com/beeware/toga/issues/2144

The `write_text` and`measure_text` methods in Canvas support multiple lines but lack control over line spacing. Adding a`line_height` argument, similar to CSS, would allow users to specify spacing as a multiple of the font size for better text layout control.

Scope (functionality and code affected).
To change this, the core (interface layer) is affected 

### Issue #2145

Title: Configurable text line height in Label

URL: https://github.com/beeware/toga/issues/2145

What is the problem or limitation you are having?
The Label accepts multiple lines, but there's no way to control their spacing.

Describe the solution you'd like
A line_height style with the same meaning as in CSS. See #2144 for a specification.

Describe alternatives you've considered
The user can split their text into multiple Labels, but because they can't be overlapped, there will be a certain minimum spacing that they can't go below.

Additional context
Compared to Canvas (#2144), the Label version of this feature would be more work to implement, but probably useful to more people.

Scope (functionality and code affected).


## Requirements for the new feature or requirements affected by functionality being refactored

Optional (point 3): trace tests to requirements.

## Code changes

### Patch

(copy your changes or the add git command to show them)

git diff ...

Optional (point 4): the patch is clean.

Optional (point 5): considered for acceptance (passes all automated checks).

## Test results

Overall results with link to a copy or excerpt of the logs (before/after
refactoring).


## UML class diagram and its description

### Key changes/classes affected

Optional (point 1): Architectural overview.

#### Core API - Canvas:
![classes_canvas](https://github.com/user-attachments/assets/fd89b88f-3903-46b6-a68f-579c1ca343ec)

#### Backend - Windows: 
![classes_windows](https://github.com/user-attachments/assets/4599bf39-775a-4073-9195-c8398f44fbb5)

#### Backend - MacOS:
![classes_macOS](https://github.com/user-attachments/assets/577b20ba-97ca-4848-b5a9-de26bd206956)

#### Backend - GTK: 
![classes_gtk](https://github.com/user-attachments/assets/a97d0993-fef3-4036-ab75-f6f36c281afc)

 #### Backend - Android:
![classes_android](https://github.com/user-attachments/assets/b154ed96-82f8-4b01-9a98-d518e015b0b7)

#### Backend - iOS: 
![classes_iOS](https://github.com/user-attachments/assets/7668e668-259e-4567-a2b5-e405294d8d1e)

#### Backend - dummy:
![classes_dummy](https://github.com/user-attachments/assets/0508bca5-2aa8-4065-ba72-7b63e6d1a889)

#### Examples - canvas:
![classes_examples](https://github.com/user-attachments/assets/9ea10a41-1417-4e4c-9ec2-af2993d161dc)


Optional (point 2): relation to design pattern(s).

## Overall experience

What are your main take-aways from this project? What did you learn?

How did you grow as a team, using the Essence standard to evaluate yourself?

Optional (point 6): How would you put your work in context with best software engineering practice?

Optional (point 7): Is there something special you want to mention here?
