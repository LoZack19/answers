def init_answers(filename: str, len_: int) -> list:
    answers = [0] * len_

    with open(filename, 'r') as infile:
        for line in infile:
            record = line.strip().split('\t')
            for i in range(len(record) // 2):
                ind = int(record[2 * i]) - 1
                answers[ind] = record[2 * i + 1]
    
    return answers


def get_answer(quiz: int, answers: list) -> str:
    ind = quiz - 1
    return answers[ind]


def main():
    answers = init_answers("answers.dat", 415)

    done = False
    while not done:
        buffer = input("> ")
        done = buffer in ['q', 'quit', 'exit']
        if not done:
            print("Answer:", get_answer(int(buffer), answers))
    

if __name__ == "__main__":
    main()