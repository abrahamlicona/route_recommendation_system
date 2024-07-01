from collections import Counter
from trajectories import trajectories
from trajectories import length_n

class Probability_Functions:
    def __init__(self):
        pass

    def find_most_common_sequence_with_prefix(self, trajectories, prefix):
        """
        Given a prefix, find the most common sequence that starts with this prefix in the trajectories.
        """
        prefix_len = len(prefix)
        candidates = [trajectory for trajectory in trajectories if trajectory[:prefix_len] == prefix]
        if candidates:
            return Counter(map(tuple, candidates)).most_common(1)[0][0]
        return None

    def find_most_common_element(self, trajectories, prefix):
        """
        Find the most common next element after the given prefix in the trajectories.
        """
        next_elements = []
        prefix_len = len(prefix)
        for trajectory in trajectories:
            for i in range(len(trajectory) - prefix_len):
                if trajectory[i:i+prefix_len] == prefix:
                    next_elements.append(trajectory[i+prefix_len])
        if next_elements:
            return Counter(next_elements).most_common(1)[0][0]
        return None

    def find_recommendation(self, input_sequence, trajectories=trajectories, length_n=length_n):
        """
        Find the recommended route based on the input sequence and trajectories.
        """

        trajectories = [t for t in trajectories if len(t) == length_n]

        result = list(input_sequence)
        
        while len(result) < length_n:
            next_element = None
            
            for i in range(len(result)):
                sub_sequence = result[i:]
                next_element = self.find_most_common_element(trajectories, sub_sequence)
                if next_element:
                    break
            
            if next_element:
                result.append(next_element)
            else:
                break

        while len(result) < length_n:
            next_element = self.find_most_common_element(trajectories, [])
            if next_element:
                result.append(next_element)
            else:
                break
        
        return result
    
# Storing class   
probability_functions = Probability_Functions()