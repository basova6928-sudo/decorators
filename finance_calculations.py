from logger import logger_path

@logger_path('finance_log.log')
def calculate_mortgage(salary, percent):
    return salary * percent / 100 * 12

@logger_path('finance_log.log')
def calculate_life_expenses(salary, percent):
    return salary * percent / 100 * 12

@logger_path('finance_log.log')
def calculate_savings(salary, mortgage, life):
    return 12 * salary - mortgage - life

if __name__ == "__main__":
    
    salary = 100000
    percent_mortgage = 30
    percent_life = 50

    mortgage = calculate_mortgage(salary, percent_mortgage)
    life = calculate_life_expenses(salary, percent_life)
    result = calculate_savings(salary, mortgage, life)

    print('Ипотека:', mortgage)
    print('Накопления:', result)
