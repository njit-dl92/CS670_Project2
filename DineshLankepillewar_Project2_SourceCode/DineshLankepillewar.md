### Steps to Run the Cluedo Game

1. **Cloning the Repository**
   - Install Git (if not installed):
     - **Linux (Ubuntu)**:
       ```bash
       sudo apt update
       sudo apt install git
       ```
   - Clone the repository:
     ```bash
     git clone git@github.com:njit-dl92/CS670_Project2.git
     ```
   
   - Navigate to the cloned repository directory:
     ```bash
     cd DineshLankepillewar_Project2_SourceCode
     ```

2. **Running the Game**
   - Ensure Python 3 is installed:
     ```bash
     python3 --version
     ```
     (If not installed, follow the instructions to install Python 3).

   - **Install Dependencies** (if applicable):
     - If there's a `requirements.txt` file, install the dependencies:
       1. Install `pip` (if not installed):
          ```bash
          sudo apt install python3-pip
          ```
       2. Install dependencies:
          ```bash
          pip3 install -r requirements.txt
          ```

   - **Run the Game**:
     - Start the game by running the command:
       ```bash
       python3 main.py
       ```

4. **Dependencies or Prerequisites**
   - **Python 3.x** is required to run the game.
   - **External Libraries** (if any) will be listed in `requirements.txt`. If there is no `requirements.txt`, the game may run without additional dependencies.
  
5. **Gameplay Instructions**
   - **Setup**: Enter the number of players (2-6), followed by player names.
   - **Card Distribution**: Cards will be distributed to each player.
   - **Main Game Loop**: Players will take turns to:
     - Move to a new room
     - Make a suggestion
     - Make an accusation
   - **End Game**: A player wins if they make a correct accusation.

