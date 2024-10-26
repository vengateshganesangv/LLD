

from parser.naive_json_parser import NaiveJsonParser
from tokenizer.naive_tokenizer import NaiveTokenizer


def main():
    parser = NaiveJsonParser(NaiveTokenizer())
    json_text = '''{"sem-2":{"Theory":{"Computer Arch":"A+","Numerical Methods":"A+"},"cgpa":"9.9","Lab":{"Parallel Computing":"A+","Computer Arch":"A+"}},"sem-1":{"Theory":{"Computer Graphics":"B","DSA":"A","Discrete Maths":"A-"},"cgpa":"9.7","Lab":{"Computer Graphics":"B","DSA":"A+","Microprocessors":"B-"}}}'''
    
    json = parser.parse(json_text)
    print(json)
    print(parser.to_string(json.get("sem-2").get("Lab").get("Parallel Computing")))

if __name__ == "__main__":
    main()