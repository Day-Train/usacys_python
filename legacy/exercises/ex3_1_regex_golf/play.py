import argparse, re, sys, os

from itertools import izip_longest

CHALLENGE_DIR = 'challenges'

def main(challenge, regex):
    if not challenge:
        challenge = raw_input('Select a challenge number: ')
    chal_words = load_challenge(challenge)
    pretty_print(chal_words)
    if not regex:
        regex = raw_input('Input regex to test: ')
    test_regex(chal_words, regex)



def load_challenge(challenge):
    result = {'good': list(), 'bad': list()}
    chal_path = os.path.join(os.curdir, CHALLENGE_DIR, challenge)
    with open(os.path.join(chal_path, 'good.txt')) as fin:
        for line in fin:
            result['good'].append(line.strip())
    with open(os.path.join(chal_path, 'bad.txt')) as fin:
        for line in fin:
            result['bad'].append(line.strip())
    return result


def test_regex(chal_words, regex):
    pattern = re.compile(regex)
    result = {'good': list(), 'bad': list()}
    for word in chal_words['good']:
        if not pattern.search(word):
            result['good'].append(word)
    for word in chal_words['bad']:
        if pattern.search(word):
            result['bad'].append(word)
    tally(chal_words, result, regex)


def tally(chal_words, result, regex):
    score = len(regex)
    score += (len(result['bad']) * 10)
    success = True if not len(result['good']) else False
    print('\n')
    if success:
        print('Your score is: {}'.format(score))
    else:
        print('Failed to match all good terms')
    word_list = {'good': list(), 'bad': list()}
    for good in chal_words['good']:
        if good in result['good']:
            good = 'x ' + good
        word_list['good'].append(good)
    for bad in chal_words['bad']:
        if bad in result['bad']:
            bad = 'x ' + bad
        word_list['bad'].append(bad)
    pretty_print(word_list)



def pretty_print(word_list):
    print('{:<20}{}'.format('Good', 'Bad'))
    print('{0:-<30}'.format(''))
    words = izip_longest(word_list['good'], word_list['bad'], fillvalue=None)
    for good, bad in words:
        print('{:<20}{}'.format(good, bad))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play Regex Golf')
    parser.add_argument('-c', '--challenge', type=str, help='Challenge to attempt')
    parser.add_argument('-r', '--regex', type=str, help='Regex to test')
    args = parser.parse_args()
    main(args.challenge, args.regex)