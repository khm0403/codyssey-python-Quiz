"""나만의 퀴즈 게임 — 한국사 편"""

import json

STATE_FILE = 'state.json'   # 프로젝트 루트에 저장되는 데이터 파일


def ask_number(prompt, low, high):
    """low~high 사이의 정수를 받을 때까지 계속 물어본다.

    공백 제거, 빈 입력, 숫자 아님, 범위 밖을 모두 여기서 처리한다.
    숫자를 입력받는 곳은 전부 이 함수를 사용한다.
    """
    while True:
        text = input(prompt).strip()

        if text == '':
            print(f'⚠  입력이 비어 있습니다. {low}-{high} 사이의 숫자를 입력하세요.')
            continue

        try:
            number = int(text)
        except ValueError:
            print(f'⚠  숫자가 아닙니다. {low}-{high} 사이의 숫자를 입력하세요.')
            continue

        if low <= number <= high:
            return number

        print(f'⚠  {low}-{high} 범위를 벗어났습니다. 다시 입력하세요.')


def ask_text(prompt):
    """비어 있지 않은 문자열을 받을 때까지 계속 물어본다."""
    while True:
        text = input(prompt).strip()

        if text:
            return text

        print('⚠  빈 입력입니다. 내용을 입력하세요.')


class Quiz:
    """퀴즈 한 문제를 표현한다. (문제 / 선택지 4개 / 정답 번호)"""

    def __init__(self, question, choices, answer):
        self.question = question    # 문제 문장 (문자열)
        self.choices = choices      # 선택지 4개 (리스트)
        self.answer = answer        # 정답 번호 1~4 (정수)

    def show(self, number):
        """문제 번호와 함께 문제와 선택지를 출력한다."""
        print(f'\n[문제 {number}] {self.question}')
        for index, choice in enumerate(self.choices, start=1):
            print(f'  {index}. {choice}')

    def is_correct(self, user_answer):
        """사용자가 고른 번호가 정답이면 True, 아니면 False."""
        return user_answer == self.answer

    def to_dict(self):
        """JSON 파일에 쓸 수 있는 딕셔너리 모양으로 바꾼다."""
        return {
            'question': self.question,
            'choices': self.choices,
            'answer': self.answer,
        }


def quiz_from_dict(data):
    """딕셔너리 하나를 Quiz 객체로 되돌린다. 형식이 이상하면 오류를 낸다."""
    question = data['question']
    choices = data['choices']
    answer = int(data['answer'])

    if len(choices) != 4 or not 1 <= answer <= 4:
        raise ValueError('퀴즈 형식이 올바르지 않습니다.')

    return Quiz(question, choices, answer)


def default_quizzes():
    """저장 파일이 없거나 손상됐을 때 사용할 기본 한국사 퀴즈 6문제."""
    return [
        Quiz('조선의 4대 왕으로 훈민정음을 창제한 인물은?',
             ['태조', '정조', '세종대왕', '영조'], 3),
        Quiz('임진왜란이 일어난 연도는?',
             ['1492년', '1592년', '1636년', '1910년'], 2),
        Quiz('고구려를 건국한 인물은?',
             ['주몽', '온조', '박혁거세', '왕건'], 1),
        Quiz('우리나라 최초의 국가인 고조선을 세운 인물은?',
             ['단군왕검', '이성계', '궁예', '대조영'], 1),
        Quiz('현존하는 세계에서 가장 오래된 금속 활자본은?',
             ['팔만대장경', '직지심체요절', '조선왕조실록', '삼국사기'], 2),
        Quiz('후삼국을 통일하고 고려를 건국한 인물은?',
             ['견훤', '궁예', '왕건', '대조영'], 3),
    ]


class QuizGame:
    """게임 전체를 관리한다. (퀴즈 목록 / 최고 점수 / 메뉴 흐름)"""

    def __init__(self):
        self.quizzes = default_quizzes()    # 퀴즈 객체들이 담긴 리스트
        self.best_score = None              # 최고 점수 (아직 안 풀었으면 None)
        self.load()                         # 저장된 데이터가 있으면 덮어쓴다

    def best_score_text(self):
        """최고 점수를 사람이 읽을 문구로 바꿔서 돌려준다."""
        if self.best_score is None:
            return '기록 없음'
        return f'{self.best_score}점'

    def load(self):
        """state.json에서 데이터를 불러온다. 실패하면 기본 퀴즈로 시작한다."""
        try:
            with open(STATE_FILE, 'r', encoding='utf-8') as file:
                data = json.load(file)

            quizzes = []
            for item in data['quizzes']:
                quizzes.append(quiz_from_dict(item))

            if not quizzes:
                raise ValueError('저장된 퀴즈가 하나도 없습니다.')

            best_score = data['best_score']
            if best_score is not None:
                best_score = int(best_score)

            self.quizzes = quizzes
            self.best_score = best_score
            print(f'\n📂 저장된 데이터를 불러왔습니다. '
                  f'(퀴즈 {len(self.quizzes)}개, 최고 점수 {self.best_score_text()})')

        except FileNotFoundError:
            print(f'\n📂 저장 파일이 없어 기본 퀴즈 {len(self.quizzes)}개로 시작합니다.')

        except (json.JSONDecodeError, KeyError, TypeError, ValueError, OSError) as error:
            self.quizzes = default_quizzes()
            self.best_score = None
            print(f'\n⚠  저장 파일이 손상되었습니다. ({error})')
            print(f'📂 기본 퀴즈 {len(self.quizzes)}개로 복구합니다.')

    def save(self):
        """퀴즈 목록과 최고 점수를 state.json에 저장한다."""
        quiz_dicts = []
        for quiz in self.quizzes:
            quiz_dicts.append(quiz.to_dict())

        data = {
            'quizzes': quiz_dicts,
            'best_score': self.best_score,
        }

        try:
            with open(STATE_FILE, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
            return True
        except OSError as error:
            print(f'⚠  저장에 실패했습니다. ({error})')
            return False

    def show_menu(self):
        """메뉴 화면을 출력한다."""
        print()
        print('=' * 40)
        print('        🎯  나만의 퀴즈 게임  🎯')
        print('=' * 40)
        print('1. 퀴즈 풀기')
        print('2. 퀴즈 추가')
        print('3. 퀴즈 목록')
        print('4. 점수 확인')
        print('5. 종료')
        print('=' * 40)

    def play(self):
        """퀴즈를 출제하고 채점한다."""
        if not self.quizzes:
            print('\n⚠  등록된 퀴즈가 없습니다. 먼저 2번에서 퀴즈를 추가해 주세요.')
            return

        total = len(self.quizzes)
        print(f'\n📝 퀴즈를 시작합니다! (총 {total}문제)')
        print('-' * 40)

        correct_count = 0
        for number, quiz in enumerate(self.quizzes, start=1):
            quiz.show(number)
            user_answer = ask_number('정답 입력: ', 1, 4)

            if quiz.is_correct(user_answer):
                print('✅ 정답입니다!')
                correct_count += 1
            else:
                correct_text = quiz.choices[quiz.answer - 1]
                print(f'❌ 틀렸습니다. 정답은 {quiz.answer}번 ({correct_text})입니다.')

            print('-' * 40)

        score = int(correct_count / total * 100)
        print('=' * 40)
        print(f'🏆 결과: {total}문제 중 {correct_count}문제 정답! ({score}점)')

        if self.best_score is None or score > self.best_score:
            self.best_score = score
            print('🎉 새로운 최고 점수입니다!')
        else:
            print(f'   (최고 점수: {self.best_score}점)')

        print('=' * 40)
        self.save()

    def add_quiz(self):
        """새 퀴즈를 입력받아 목록에 추가하고 파일에 저장한다."""
        print('\n📌 새로운 퀴즈를 추가합니다.')

        question = ask_text('문제를 입력하세요: ')

        choices = []
        for number in range(1, 5):
            choices.append(ask_text(f'선택지 {number}: '))

        answer = ask_number('정답 번호 (1-4): ', 1, 4)

        self.quizzes.append(Quiz(question, choices, answer))

        if self.save():
            print(f'✅ 퀴즈가 추가되었습니다! (현재 총 {len(self.quizzes)}개)')
        else:
            print('⚠  목록에는 추가됐지만 파일 저장에 실패했습니다.')

    def show_list(self):
        """등록된 퀴즈 목록을 보여준다."""
        if not self.quizzes:
            print('\n⚠  등록된 퀴즈가 없습니다. 먼저 2번에서 퀴즈를 추가해 주세요.')
            return

        print(f'\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)')
        print('-' * 40)

        for number, quiz in enumerate(self.quizzes, start=1):
            print(f'[{number}] {quiz.question}')

        print('-' * 40)

    def show_score(self):
        """최고 점수를 보여준다."""
        if self.best_score is None:
            print('\n⚠  아직 퀴즈를 푼 기록이 없습니다. 먼저 1번에서 퀴즈를 풀어보세요.')
            return

        print(f'\n🏆 최고 점수: {self.best_score}점')

    def run(self):
        """메뉴를 반복해서 보여주고, 선택한 기능을 실행한다."""
        while True:
            self.show_menu()
            choice = ask_number('선택: ', 1, 5)

            if choice == 1:
                self.play()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                self.save()
                print('\n💾 저장했습니다. 게임을 종료합니다. 안녕히 가세요!')
                break


def main():
    """프로그램의 시작점."""
    game = QuizGame()
    game.run()


if __name__ == '__main__':
    main()
