# /usr/bin/env python
import re
import splunk.Intersplunk as si

def validate_args(keywords, argvals):
    # validate args
    ALLOWED_OPTIONS = ['fields']
    illegal_args = filter(lambda x: x not in ALLOWED_OPTIONS, argvals)
    if len(illegal_args) != 0:
        exit("The argument(s) '%s' is invalid. Supported arguments are: %s" % (illegal_args, ALLOWED_OPTIONS))


if __name__ == '__main__':
    results = si.readResults(None, None, False)
    keywords, argvals = si.getKeywordsAndOptions()
    validate_args(keywords, argvals)

    fields_to_replace = argvals['fields'].split(",")
    for token in fields_to_replace:
        for row in results:
            token_fields = re.findall('\$(?P<token>[^$]+)\$', row[token])
            normalized_text = row[token]
            for t in token_fields:
                if t in row:
                    normalized_text = normalized_text.replace('$%s$'%t, row[t])
            row[token + '_normalized'] = normalized_text

    si.outputResults(results)
