import site

def find(calc, x):
    try:
        return calc.index(x)
    except:
        return 1000000

def natural(x):
    a = float(x)
    return 1000000 * a**(1/1000000) - 1000000

def sine(x):
    a = float(x)
    t = 1
    fac = 1
    sin = 0
    while t < 100:
        sin += a**t/fac
        fac *= (t + 1) * (t + 2)
        t += 2
        sin -= a**t/fac
        fac *= (t + 1) * (t + 2)
        t += 2
    return sin

def math(term):
    try:
        while 'ln' in term:
            a = find(term, 'ln')
            term[a] = natural(term[a + 1])
            term.pop(a + 1)
        while 'log' in term:
            a = find(term, 'log')
            term[a] = natural(term[a + 1]) / natural(10)
            term.pop(a + 1)
        while 'sin' in term:
            a = find(term, 'sin')
            term[a] = sine(term[a + 1])
            term.pop(a + 1)
        while 'cos' in term:
            a = find(term, 'cos')
            term[a] = sine(pi/2 - float(term[a + 1]))
            term.pop(a + 1)
        while 'tan' in term:
            a = find(term, 'tan')
            term[a] = sine(term[a + 1]) / sine(pi/2 - float(term[a + 1]))
            term.pop(a + 1)
        while 'csc' in term:
            a = find(term, 'sin')
            term[a] = 1 / sine(term[a + 1])
            term.pop(a + 1)
        while 'sec' in term:
            a = find(term, 'cos')
            term[a] = 1 / sine(pi/2 - float(term[a + 1]))
            term.pop(a + 1)
        while 'cot' in term:
            a = find(term, 'cot')
            term[a] = sine(pi/2 - float(term[a + 1])) / sine(term[a + 1])
            term.pop(a + 1)
        while '^' in term:
            a = find(term, '^')
            term[a] = float(term[a - 1]) ** float(term[a + 1])
            term.pop(a - 1)
            term.pop(a)
        while '*' in term or '/' in term:
            a = find(term, '*')
            b = find(term, '/')
            if a < b:
                term[a] = float(term[a - 1]) * float(term[a + 1])
                term.pop(a - 1)
                term.pop(a)
            elif b < a:
                term[b] = float(term[b - 1]) / float(term[b + 1])
                term.pop(b - 1)
                term.pop(b)
        while '+' in term or '-' in term:
            a = find(term, '+')
            b = find(term, '-')
            if a < b:
                term[a] = float(term[a - 1]) + float(term[a + 1])
                term.pop(a - 1)
                term.pop(a)
            elif b < a:
                term[b] = float(term[b - 1]) - float(term[b + 1])
                term.pop(b - 1)
                term.pop(b)
        return float(term[0])
    except TypeError:
        None

num = ['0', '1', '2', '3', '4,', '5', '6', '7', '8', '9']
oper = ['+', '-', '*', '/', '^', '(', ')', 'log', 'ln', 'sin', 'cos', 'tan', 'csc', 'sec', 'cot']
function = ['log', 'ln', 'sin', 'cos', 'tan', 'csc', 'sec', 'cot']
e = '2.7182818284590452'
pi = 3.1415926535897932

print("Yep. It's a calculator. As if we've never used technology for that before.\n\nThis calculator understands spacing, parentheses, negative numbers, Euler's number ('e'), pi ('pi'), logarithms, and trigonometric functions.\nAny parentheses must be smooth (). No brackets [] or fancy brackets {}.\nWhen using e or pi, use operators to attach e to other numbers. For example, the computer will understand 2 * e, but not 2e.\nWhen using trig functions, use the standard sin, cos, tan, csc, sec, and cot abbreviations, followed by the input.\nWhen using logarithms, type 'ln' to use natural log, and 'log' for base 10. If you wish to use other logarithm bases, well, I hoped you paid attention to logarithm properties!\n")

while True:
    calc = input("Please enter your calculation: ")
    mem = calc
        
    for x in oper:
        calc = calc.replace('e', e)
        calc = calc.replace('pi', str(pi))
        calc = calc.replace(x, ' ' + x + ' ')
    calc = calc.split()
    if num not in calc or e in calc and function not in calc:
        print("No, I don't except words. If you're not going to do this properly, I quit.")
        exit()
    
    minus = [i for i, x in enumerate(calc) if x == "-"]
    minus.reverse()

    for x in minus:
        if x == 0 or calc[x - 1] in oper and calc[x - 1] != ')':
            calc[x + 1] = '-' + str(calc[x + 1])
            calc.pop(x)
    
    while ')' in calc:
        end = find(calc, ')')
        begin = end
        while begin > 0:
            begin = begin - 1
            if calc[begin] == '(':
                break
        calc[begin] = math(calc[begin + 1:end])
        for x in range(end - begin):
            calc.pop(begin + 1)
    if len(calc) > 1:
        math(calc)

    print(mem + " = " + str(calc) + "\n")
