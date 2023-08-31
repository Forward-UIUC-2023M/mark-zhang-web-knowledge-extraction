import asyncio
from dataclasses import dataclass
# import logging
# logging.basicConfig(level=logging.DEBUG)

from dotenv import load_dotenv
load_dotenv()

from cot import qa

@dataclass
class Answer:
    contain: set[str]
    not_contain: set[str]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


tests = [
    {
        'file': 'cs_faculty.html',
        'question': 'Give me a list of all the faculty members with the title "teaching associate professor".',
        'answer': Answer(
            {'Mattox Alan Beckman', 'Geoffrey Werner Challen', 'Wade A. Fagen-Ulmschneider', 'Geoffrey Lindsay Herman', 'Marco Morales Aguirre', 'Eric Gene Shaffer', 'Mariana Silva'},
            {'8'}
        ),
    },
    {
        'file': 'cs_faculty.html',
        'question': 'Give me a list of all the faculty members with the title "teaching assistant professor".',
        'answer': Answer(
            {'Abdussalam Alawini', 'Benjamin Cosman', 'Neal E. Davis', 'Carl Evans', 'Yael Gertner', 'Hongye Liu', 'Michael Nowak', 'Brad R. Solomon', 'Ruby Tahboub'},
            {'10'}
        ),
    },
    {
        'file': 'undergrad_advising.html',
        'question': 'Who is the undergraduate program coordinator?',
        'answer': Answer(
            {'Heather Zike'},
            {}
        ),
    },
    {
        'file': 'undergrad_advising.html',
        'question': 'Who has/have the title "Undergraduate Academic Advisor"?',
        'answer': Answer(
            {'Jacob Deters', 'Fabian A. Zermeno Yerenas', 'Jenn Rose'},
            {},
        ),
    },
]


async def evaluate(test):
    output = await qa(test['file'], test['question'])
    errors = []
    for s in test['answer'].contain:
        if s not in output:
            errors.append(f'Answer "{s}" not in output')
    for s in test['answer'].not_contain:
        if s in output:
            errors.append(f'Answer "{s}" in output')

    if len(errors) > 0:
        print(
            bcolors.FAIL + \
            f'Failed test {test["question"]} on file {test["file"]}:\n' + \
            '\n'.join(['\t' + e for e in errors]) + \
            bcolors.ENDC
            )
    else:
        print(
            bcolors.OKGREEN + \
            f'Passed test {test["question"]} on file {test["file"]}' + \
            bcolors.ENDC
            )


async def main():
    await evaluate(tests[1])
    # for test in tests:
    #     await evaluate(test)


if __name__ == '__main__':
    asyncio.run(main())