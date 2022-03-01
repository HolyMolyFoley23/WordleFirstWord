import os
from collections import Counter

def array_of_words(filepath):
    data = []
    f = open(filepath,'r')
    for x in f:
        data.append(x.strip())
    f.close()
    return data

def write_words(word_data):
    word_data.sort(key = lambda x:x[2])
    word_data.sort(key = lambda x:x[1])
    arr = []
    arr.append(f"Word  Worst  Mean")
    for x,y,z in word_data:
        arr.append(f"{x} {y:5d}  {z:.2f}")
    text = "\n".join(arr)
    f = open(r'ordered_words.txt',"w")
    f.write(text)
    f.close()

def greens(guess,solution):
    return [x if x==y else "." for x,y in zip(guess,solution)]

def yellows(guess,solution):
    sol_letters = Counter(solution)
    data = ['.'] * 5
    
    #Handle special case with green but no yellow
    for gus,sol in zip(guess,solution):
        if(gus == sol):
            sol_letters[gus] -= 1
            
    for i, (gus,sol) in enumerate(zip(guess,solution)):
        if(gus != sol):
            if(gus in sol_letters):
                if(sol_letters[gus] > 0):
                    sol_letters[gus] -= 1
                    data[i] = gus
                else:
                    data[i] = str.upper(gus)
    return data

def grays(guess,solution):
    return set(guess) - set(solution)

def tuple_info(guess,solution):
    tup_greens = "".join(greens(guess,solution))
    tup_yellows = tuple(yellows(guess,solution))
    tup_grays = "".join(sorted(list(grays(guess,solution))))
    return (tup_greens,tup_yellows,tup_grays)

def generate_word_data(guesses,solutions):
    word_data = []
    for guess in guesses:
        guess_buckets = Counter(tuple_info(guess,sol) for sol in solutions)
        word_data.append((guess,guess_buckets.most_common(1)[0][1],(len(solutions) - 1) / (len(guess_buckets) - 1)))
    return word_data
    
def main():
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    guess_file = os.path.join(curr_dir,r'wordlist_guesses.txt')
    solution_file = os.path.join(curr_dir,r'wordlist_solutions.txt')
    guess_words = array_of_words(guess_file)
    solution_words = array_of_words(solution_file)
    write_words(generate_word_data(guess_words,solution_words))

if __name__ == "__main__":
    main()
