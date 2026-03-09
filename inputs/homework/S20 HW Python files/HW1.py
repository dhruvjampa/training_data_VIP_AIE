from haystack import Document


homework_sections = [
    {
        "title": "Homework 1 Introduction",
        "content": """Welcome to ECE 20875, Python for Data Science! In this class, you will learn the basics of various topics in data science, and, along the way, learn how to write code in Python.""",
        "tags": ["introduction", "python", "data science"]
    },
    {
        "title": "Homework Goals",
        "content": """This homework has several objectives:

1. Get familiar with git and GitHub: cloning, committing, tagging, etc.
2. Get familiar with the GitHub Classroom submission system.
3. Write a simple Python script demonstrating Python fundamentals.""",
        "tags": ["objectives", "git", "github", "python"]
    },
    {
        "title": "Version Control in Git",
        "content": """Git is a version control tool. What is version control? It is a means of retaining organized versions of your code as you work on a project. This is especially important in industry for code organization, collaborative projects, and large projects spanning many files. 
Further information on how GitHub might be used in collaborative projects can be found at https://guides.github.com/ if interested. You will not be concerned with branches in this class.

When working with repositories for this class, there are three main parts to working with git: 
1. The remote repository (on GitHub) 
2. The local repository (on your device/ Scholar account) 
3. Your working files (on your device/ Scholar account) 

**Note:** Git is the tool you use to do version control. GitHub is where your remote repository is hosted.

When you do a `git add` followed by `git commit`, you are updating your local repository.
When you do a `git push`, you are updating the remote repository on GitHub (supervisors or collaborators can now see your changes).

The key commands you will need to use in this assignment (and at other times) are:

1. `git clone`: This sets up a local repository on your machine by "cloning" (copying) a remote repository; in this case, a repository set up on GitHub.
2. `git add`: When you have changed a file, you can "stage" it for the next version using this command.
3. `git commit`: Creates a new version of your code. This version exists only in your local repository.
4. `git push`: Updates the remote repository (on GitHub) with all the changes that you have `commit`ted to your local repository.
5. `git pull`: Updates your local repository with any changes that are on GitHub.
6. `git status`: Shows the status of any files in your local repository.

**Push your code to GitHub often.** Not only does that prevent you from losing any code if you accidentally delete anything, but it also helps us help you debug by giving us access to your latest code.

**NOTE:** You should verify that your code files are showing up correctly on GitHub once you have `push`ed them from your local machine.""",
        "tags": ["git", "version control", "github", "repository"]
    },
    {
        "title": "Python Fundamentals",
        "content": """Familiarize yourself with basic Python scripting from the lecture notes. The Python language documentation is online at https://docs.python.org/3/

This assignment has the potential to involve:
- Initializing variables. Recall that unlike C, C++, etc., Python does not require a data type declaration.
- Arithmetic (+,-,*,/,%,**,//), logical (`and`,`or`,`not`), and comparison (<,>,<=,>=,==,!=) operations.
- Decision (`if`, `elif`, `else`) structures.
- A basic understanding of lists and how to index them.

**A caution:** DO NOT use `&` and `|`. They are for bitwise operations, which should not be used for conditional statements.

Example:
```python
if True:
    print('HW1 is truly fantastic.')
print('I concur.')
```""",
        "tags": ["python", "fundamentals", "data types", "control structures"]
    },
    {
        "title": "Getting Started with Homework",
        "content": """Clone your HW1 repository by clicking on the GitHub classroom link distributed through Piazza. This will create a repository on GitHub with your username. Use `git clone` to clone that repository locally. If you face issues with this, then you might want to look into using 'ssh key' to clone (directions at the end of README).

There should be three files in your repository when you begin:
1. This README file.
2. `problem1.py`, a python file with one line of code, which contains a single year.
3. `problem2.py`, a python file that has questions you must answer using the format specified in the file.""",
        "tags": ["git", "github", "repository", "cloning"]
    },
    {
        "title": "Problem 1 - Leap Year Calculation",
        "content": """Modify `problem1.py` by adding additional lines of code so that it solves the following problem:
Determine if the year given at the top of the file in `problem1.py` is a leap year.

**Leap Year Rules:**
- A leap year is when the year is divisible by 4, **but not divisible by 100 unless also divisible by 400**.

Example test cases:
- Year `8` → `True`
- Year `2010` → `False`
- Year `1200` → `True`

**Important:** Your code should work for any given year.""",
        "tags": ["python", "leap year", "conditional statements", "math logic"]
    },
    {
        "title": "Using SSH for GitHub",
        "content": """If HTTPS cloning fails, set up an SSH key:

1. Run: `ssh-keygen -t rsa -C "your_email@example.com"`
   - Ensure `"your_email@example.com"` is the same email used on GitHub.

2. Press "Enter" when prompted where to store keys. This will save the keys in the default location.

3. Enter a secure passphrase that you will remember.

4. Keys will be saved in `.ssh/`.

Now, you must enter your public key on GitHub:
- Navigate to GitHub.
- Click on your profile picture → **Settings** → **SSH and GPG Keys**.
- Click **New SSH Key**.
- Create a title so you will know which computer the SSH key corresponds to.
- Paste the **public key**.
- Click **Add SSH Key**.

For more help: https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account""",
        "tags": ["ssh", "github", "authentication", "security", "git"]
    }
]

haystack_documents = [
    Document(
        content=section["content"], 
        meta={"title": section["title"], "source": "homework_1", "course": "ECE 20875", "tags": section["tags"]}
    )
    for section in homework_sections
]

print(haystack_documents)