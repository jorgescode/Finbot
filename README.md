# Planned Features
1. Collecting and storing game info from users
2. Detecting which users are in the channel when it is called
3. Giving random suggestions of games that all users have in common

## Feature 1
### Collecting and storing game info from users
- create db of users and their games
- accept info from users
- CRUD of games for each user

## Feature 2
### Detecting which users are in the voice channel when it is called
- detect voice channel being called in
- detect users in identified channel

## Feature 3 (not completely using discord api)
### Giving random suggestions of games that all users have in common
- store user games in set
- use intercept or set operations to find common games
- select random game from union set
- output list of available games
- recommend a random game
- output any users missing, and show a tip for how to add games to the bot