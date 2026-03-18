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

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
