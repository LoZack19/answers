def init_answers(filename: str) -> list:
    answers = []

    with open(filename, 'r') as infile:
        answers = infile.readline().strip().split(';')
    
    return answers


def get_answer(buffer: str, answers: list) -> str:
    answer = None

    try:
        ind = int(buffer) - 1
        answer = answers[ind]
    except IndexError as err:
        print("Quiz", buffer, "not found")
    except ValueError as err:
        print("Invalid quiz number")
    
    return answer


def main():
    answers = init_answers("answers.txt")

    done = False
    while not done:
        buffer = input("> ")
        done = buffer in ['q', 'quit', 'exit']
        if not done:
            answer = get_answer(buffer, answers)
            if answer != None:
                print("Answer:", answer)
    

if __name__ == "__main__":
    main()