# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  The game looks nice on the webpage, and it provides settings that users can change the difficulty levels when playing and users can ask for hints. Moreover, users can look up the developer debug info for the target answer.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. when I ran the game, the first thing I noticed was that the hint message was wrong. Hint messages always say go higher when the target number is lower than the guessing number. It should tell users to go higher if their guessings are lower than the target number and to go lower if their guessings are higher than the target number.
  2. The second thing I noticed was that I can not submit my guesses after restarting a new round of the game. It should enable users to start a new game after each round.
  3. The third thing I noticed was that the attempt number can be negative. When the attempt is empty, the game should be ended and force the user to either stop playing or starting a new game.
  4. The forth thing I noticed was that the change of difficulty levele does not change the target number accordingly. If users change the difficulty levels, the target number should also be selected from a corresponding range.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

  I used Copilot as my AI tool on this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

  In the problem of the hint message does not correcly help users, AI said the logic of print statements are wrong, such as "Go Higher" when the guess is bigger than the target, or "Go Lower" when the guess is smaller than the target. AI suggested to modify those comments, such that "Go Higher" when the guess is smaller than the target, and "Go Lower" when the guess is higher than the target. I varified the origional code and agree with AI because those print messages do not comply with the logic statements.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

  One incorrect AI suggestion was the import code in test_game_logic.py. The AI assumed that methods from logic_utils.py could be imported directly, but that failed because the two files were in different directory levels. I verified this by running the test file, reading the error message, and checking the project structure.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

  I would go to look up the code first to see if the logic is right or not. Then, I will try to look up the test cases if available. Lastly, I will look up the actual functions on the webpage to see if the bug is still there or not.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  In test_game_logic.py, AI generates one test case that I especially care about is testing if the hint messages actually correctly guiding users in their guessings, and those tests are: test_to_high(), test_to_low(), and test_win(). Those test cases all passed and it means the bug of misleading hint messages is fixed.
- Did AI help you design or understand any tests? How?

  Yes, AI helped me to design better, especially in the refactoring process. It helped me to move methods that are handling modifying and varifying user inputs into logic_utils.py. Otherwise, methods of processing data with methods of handling UI will be mixed together and messy for us seperating the responsibilities of each methods.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

  In the original app, the secret number is tied to a hardcode range of 1 to 100. And this caused that the secret number does not align with the difficulty level range. Also, there was a code that resets the secret number everytime when the attems % 2 == 0, and this is the main reason that the secret number changes all the time in the game.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit works by rerunning the whole Python script every time the user interacts with the app, such as clicking a button, typing in a box, or changing a selection. That means the page is rebuilt again and again based on the latest input. Session state is what lets Streamlit remember information across those reruns, such as a user’s score, previous guesses, or whether a game has already ended. Without session state, those values would reset each time the script reruns. So, reruns make the app interactive, and session state gives the app memory during the user’s visit.
- What change did you make that finally gave the game a stable secret number?

  We fixed the unstable secret number by removing the logic that changed the secret’s data type based on whether the attempt number was even or odd. Instead of sometimes converting the secret number to a string, we now always compare the guess to st.session_state.secret directly as the same value throughout the game session. This made the secret number stable for each game.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  One habit I want to reuse in future labs and projects is using AI to help summarize commit messages. I found that AI-generated commit messages can capture many important details about the changes made in the code, which makes it easier to document progress clearly.
- What is one thing you would do differently next time you work with AI on a coding task?

  Next time, I would more carefully double-check the code generated or modified by AI before finalizing my work. I learned that AI can sometimes produce non-working code or fail to catch existing bugs, so review and testing are still necessary.
- In one or two sentences, describe how this project changed the way you think about AI generated code.

  This project changed the way I think about AI-generated code by showing me that AI can be helpful and efficient, but it is not always reliable. Even when the code looks correct, I still need to review, test, and verify it carefully.
