import os, argparse

parser = argparse.ArgumentParser()
parser.add_argument("--data", "-d", default=None, type=str, required=True,
                    help="The input data file, e.g., 'data/XNLI/test.tsv'.")
parser.add_argument("--output_dir", "-o", default=None, type=str, required=True, help="The output directory.")
args = parser.parse_args()

LG = 'en'

out_file_path = os.path.join(args.output_dir, 'xnli-en', 'test_matched.tsv')
out_dir = vars(args)['output_dir']

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open(args.data, 'r') as fin, open(out_file_path, 'w') as fout:
    headline = next(fin)
    fout.write(headline)
    header = {col: i for i, col in enumerate(headline.strip().split('\t'))}
    for i, line in enumerate(fin):
        cells = line.split('\t')
        if cells[header['language']] == LG:
            fout.write(line)
