# Agent Minds

Developing accurate and intelligent agents for Pac-Man requires a solid understanding of the game in order to replicate the behaviour of ghosts and also the translation of Pac-Man's behaviours into a rule-based system.

The system has been developed with the intention of allowing hot-swappable agents. This was done so that the application was not coupled to one single agent and so this would allow me to try various different models. The base starting point will be to develop a rule-based agent, while future iterations will look to include some interpretation of a reinforcement learning agent. The hot-swapping also applies to ghosts. It is left open so that should I want to be able to adapt ghost behaviours or even look at developing intelligent ghosts, then this would be possible.

## Game Facts

- All agents have awareness of the entire environment at any time

## Pac-Man

### Core Concepts

Pac-Man is user-controlled, therefore, there are no set rules or behaviours which must be followed. It is totally up to the interpretation of the player. Also, unlike the ghosts, Pac-Man does not have a single target and therefore the decision making at each tick is completely open-ended. Pac-Man's only goal is to collect all of the Pac-Dots without losing all of its lives.

To define this better, Pac-Man should visit all positions on the map which contain a pickup item whilst avoiding contact with ghosts.

### Traditional Theories

There are well-documented [solution patterns](https://www.classicgaming.cc/classics/pac-man/play-guide) for Pac-Man to complete the levels. However, these traditional solutions will not work in this project for a number of reasons:

1) All of the solutions describe exact points and paths that Pac-Man should follow. This is unsuitable for an intelligent agent as no decision making is taking place, the path is already established for them.
2) Ignoring the above issue, these paths (especially at higher levels with faster ghosts) can become "move-perfect" meaning that they are designed to, in some cases, dodge ghosts by a single space in order to make the most effective move. This does not translate from the original game into my version because I am not working on the traditional timing of the game but working with my own implementation of "ticks"

It is therefore obvious, from the above, that I will need to look instead at behaviours and concepts instead of existing solutions if I wish to learn and inherit ideas into making my own solutions.

### Solutions

*The following descriptions apply to a rule-based agent system*

One of the simplest rule-based systems to implement would use a searching algorithm with a heuristic function to quickly filter / decide between paths. The heuristic function I am implementing is a simple path reward value. This reward is a sum of all of the pickup items between the start and end point.

Taking the solution chronologically, one of the hardest decisions the agent will have to make is the starting direction. The image below shows the number of possible paths that Pac-Man could take within 10 ticks.

![Pac-Man Paths](images/pacman-level-high-res.jpg)

As can be seen, there are ten different paths which are possible within 10 game ticks. Even increasing this example by one game tick takes the possible starting options up to 18. Of the displayed ten paths, eight would have an equal reward value and therefore using the reward value alone, Pac-Man would not be able to make a decision on which way to go.
