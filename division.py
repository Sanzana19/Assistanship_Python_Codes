import argparse

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog='División',
        description='Programa que divide dos números.',
        epilog='Ayudantía 01'
    )
    parser.add_argument('-n', help='Numerador', type=float)
    parser.add_argument('-d', help='Denominador (debe ser distinto de 0)', type=float)
    return parser.parse_args()

def dividir(n: float, d: float) -> float:
    if d == 0:
        print('El denominador no puede ser 0')
        return 0
    else:
        return n/d

def main() -> None:
    args = get_args()
    print(dividir(args.n, args.d))

if __name__ == '__main__':
    main()
