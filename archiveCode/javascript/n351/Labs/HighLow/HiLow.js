/**************************************
TITLE: Lab #1 High Low
AUTHOR: Robert Nathan Boyd (RNB)
CREATE DATE: 2011.07.03
PURPOSE:Generate a (mostly) random number between 1 - 100. 
	Ask the user if they want to play a game.
	If they say no, ask them to come back some other time
	If they say yes, launch the Hi-Lo game
	Describe the Hi-Lo game to the user 
	Prompt the user for a number
	Compare the user guess to the secret number
	Tell the user whether their guess was Too High, Too low, or correct.
	Keep track of how many tries it takes to guess the number
	ask them if they would like to play again. 
	If they answeryes, 
		re-launch the game. 
		If they say no, thank them for playing and tell them you hope to see them again soon.
	Follow proper coding conventions. (See lab expectations guide)
	Extra credit ie, parameter passing with functions, control structure usage, etc.), as well as artistry of the hosting web page.

LAST MODIFIED ON: 2011.07.03
LAST MODIFIED BY: Robert Nathan Boyd (RNB)
MODIFICATION HISTORY:
2011.07.04	updated documentation
2011.07.13  changed interface
**************************************/  

/**************************************
TITLE: gameIntroduction
AUTHOR: Robert Nathan Boyd
DESCRIPTION: 	Ask the user if they want to play a game.
		If they say yes, launch the Hi-Lo game
		Describe the Hi-Lo game to the user
		Prompt the user for a number
		Keep track of how many tries it takes to guess the number

@param	NA

@return NA
**************************************/ 

function gameIntroduction(booNewGame) {
    //user response
	
	if(booNewGame == true){
		strPrompt = "Would you like to play a game?";
	} else {
		strPrompt = "Would you like to play again?";
	}//end if else
	
    strPlayGame = prompt(strPrompt);
    strPlayGame = strPlayGame.toUpperCase();    
    
    if(strPlayGame == "YES"){
	intUserGuess = 0; //Users Guess
	intGuesses = 0; //Number of guess attempts by user
	intRandNum = secretNumberGen(); // random secret number

	alert("The goal of this game is for you to guess my number. Its simple really. You just enter a number and I will tell you if you are high or low. Try to guess my numbes in just a few guesses.");

	while(intUserGuess != intRandNum){
	    intGuesses++;
	    intUserGuess = prompt("Guess a number between 1 and 100");
	    strVerdict = processGuess(intRandNum, intUserGuess); //represents the relationship of the guess to the secret number
	    alert("Your guess was " + strVerdict);

	    if (strVerdict == "correct!"){
		processReward(intGuesses);

	    }//end if

	}//end while
	gameIntroduction(false);

    } else {
	checkPlayGame(strPlayGame);

    }//end else

}//end function

/**************************************
TITLE: checkPlayGame
AUTHOR: Robert Nathan Boyd
DESCRIPTION: 	Checks the user response 
		If they say no, ask them to come back some other time
		If they respond with something outside of scope prompt them again

@param strPlayGame	user response to play game?

@return NA
**************************************/ 

function checkPlayGame(strPlayGame) {

    if(strPlayGame == "NO"){
	alert("Goodbye. Come back another time.");

    } else {
	alert("I did not understand your response");
	gameIntroduction();

    }//end else

}//end function

/**************************************
TITLE: secretNumberGen
AUTHOR: Robert Nathan Boyd
DESCRIPTION: Generates a random number 

@param NA

@return intRandNum	random number from 1:100
**************************************/ 

function secretNumberGen() {
    intRandNum = Math.ceil(Math.random() * 100);
    return intRandNum;

}//end function

/**************************************
TITLE: processGuess
AUTHOR: Robert Nathan Boyd
DESCRIPTION: Determine if the user's guess is higher or lower than the comp random number

@param intRandNum	number generated by random number generator
@param intUserGuess	number guessed by the user

@return low		user guessed too low
@return high	user guessed too high
@return correct	user guessed correctly
@return else	user entered an out of scope guess
**************************************/ 

function processGuess(intRandNum, intUserGuess) {
    if(intUserGuess < intRandNum){
	return "low";
    } else if ( intUserGuess > intRandNum){
	return "high";
    } else if (intUserGuess == intRandNum){
	return "correct!";
    } else {
	return "not a number between 1 and 100 guess again";

    }//end else

}//end function

/**************************************
TITLE: gameIntroduction
AUTHOR: Robert Nathan Boyd
DESCRIPTION: Reward the user by telling them how many guesses it took them to guess the number

@param intGuesses number of guess attempts made by the user

@return NA
**************************************/ 

function processReward(intGuesses) {
    alert("It took you " + intGuesses + " guesses");

}//end function

gameIntroduction(true);