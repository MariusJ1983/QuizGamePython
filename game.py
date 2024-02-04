import pygame
import sys

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT = pygame.font.Font(None, 36)

# Question data (replace with your own questions and image paths)
questions = [
    {
        "prompt": "Who was the first President of the United States?",
        "options": ["George Washington", "Thomas Jefferson", "John Adams"],
        "correct_option": "George Washington",
        "background_image": "background1.jpg"
    },
    {
        "prompt": "In what year did World War II end?",
        "options": ["1943", "1945", "1947"],
        "correct_option": "1945",
        "background_image": "background2.jpg"
    },
    {
        "prompt": "Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen"],
        "correct_option": "William Shakespeare",
        "background_image": "background3.jpg"
    },
    # Add more questions as needed
]

# Game setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("History Quiz")
clock = pygame.time.Clock()

class Question:
    def __init__(self, prompt, options, correct_option, background_image):
        self.prompt = prompt
        self.options = options
        self.correct_option = correct_option
        self.background_image = background_image

# Convert the data into Question objects
quiz_questions = [Question(q["prompt"], q["options"], q["correct_option"], q["background_image"]) for q in questions]

# Game loop
def run_quiz():
    score = 0
    current_question_index = 0

    while current_question_index < len(quiz_questions):
        question = quiz_questions[current_question_index]

        # Load background image
        background_image = pygame.image.load(question.background_image)
        background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

        # Display background
        screen.fill(WHITE)

        # Display image on one half
        image_rect = background_image.get_rect()
        image_rect.width //= 2
        screen.blit(background_image, (0, 0), pygame.Rect(0, 0, image_rect.width, image_rect.height))

        # Display question on the other half
        question_text = FONT.render(question.prompt, True, BLACK)
        screen.blit(question_text, (WIDTH // 2, 50))

        # Display answer options
        for i, option in enumerate(question.options, start=1):
            option_text = FONT.render(f"{i}. {option}", True, BLACK)
            screen.blit(option_text, (WIDTH // 2, 100 + i * 40))

        pygame.display.flip()

        # Wait for user input
        user_answer = None
        while user_answer is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if pygame.K_1 <= event.key <= pygame.K_9:
                        user_answer = event.key - pygame.K_1

        # Check the answer
        if question.options[user_answer] == question.correct_option:
            score += 1

        current_question_index += 1

    display_result(score)

def display_result(score):
    screen.fill(WHITE)

    result_text = FONT.render(f"Your score: {score}/{len(quiz_questions)}", True, RED)
    screen.blit(result_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    pygame.display.flip()

    # Wait for a few seconds before quitting
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Run the quiz
run_quiz()
