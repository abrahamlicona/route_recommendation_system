# Route Recommendation System

This repository contains a route recommendation system based on sequence occurrence. The system analyzes a set of trajectories and recommends the most likely continuation for a given input route. 

## Repository Structure

The repository is divided into four main files:

1. **main.py**
2. **prob_functions.py**
3. **help_functions.py**
4. **trajectories.py**

### main.py

The main entry point of the application. It contains the `Menus` class that handles user interaction and input processing.

#### `Menus` Class
- **Attributes:**
  - `trajectories`: List of predefined trajectories.
  - `valid_nodes`: List of valid nodes.
  - `route_length`: The required length of the route.

- **Methods:**
  - `route_menu()`: Handles user input for route entry and displays recommendations.
  - `main_menu()`: Displays the main menu and navigates to the route menu.

### prob_functions.py

This file contains the core logic for calculating route recommendations based on the input sequence.

#### `Probability_Functions` Class
- **Methods:**
  - `find_most_common_sequence_with_prefix(trajectories, prefix)`: Finds the most common sequence starting with the given prefix.
  - `find_most_common_element(trajectories, prefix)`: Finds the most common next element following the given prefix.
  - `find_recommendation(input_sequence, trajectories, length_n)`: Generates a recommended route by extending the input sequence.

##### Mathematical Formulas

1. **Finding the Most Common Sequence with a Prefix:**
   Given a prefix $\( p \)$, find the most common sequence $\( S \)$ in the trajectories:
   $\[
   S = \arg\max_{s \in \text{candidates}} \text{Count}(s)
   \]$
   where $\(\text{candidates} = \{t \mid t[:\text{len}(p)] = p, t \in \text{trajectories}\}\)$.

2. **Finding the Most Common Next Element:**
   Given a prefix $\( p \)$, find the most common next element $\( e \)$ in the trajectories:
   $\[
   e = \arg\max_{e \in \text{nextelements}} \text{Count}(e)
   \]$
   where $\(\text{nextelements} = \{t[i+\text{len}(p)] \mid t[i:i+\text{len}(p)] = p, t \in \text{trajectories}, 0 \leq i < \text{len}(t) - \text{len}(p)\}\)$.

3. **Finding the Recommended Route:**
   Extend the input sequence \( r \) to the desired length \( n \):
   \[
   r' = r + [\text{next\_element}(r)]
   \]
   until \(\text{len}(r') = n\), where \(\text{next\_element}(r)\) is found using the most common next element method.

### help_functions.py

Contains helper functions for clearing the screen and displaying menus.

#### `Help_Functions` Class
- **Methods:**
  - `clear_screen(n)`: Clears the console screen.
  - `menu(title, context, num_options, text_array, option_message)`: Displays a menu with the given options.

### trajectories.py

Defines the set of trajectories and valid nodes used in the recommendation system.

- **trajectories**: List of predefined trajectories.
- **valid_nodes**: List of valid nodes.
- **length_n**: Required length of the route.

## Usage

1. Run the `main.py` script.
2. Follow the prompts to enter a route.
3. The system will recommend the most likely continuation of the route based on the predefined trajectories.
