import difflib,time

def split_by_sep(seq):
    """
    This method will split the HTTP response body by various separators,
    such as new lines, tabs, <, double and single quotes.

    This method is very important for the precision we get in chunked_diff!

    If you're interested in a little bit of history take a look at the git log
    for this file and you'll see that at the beginning this method was splitting
    the input in chunks of equal length (32 bytes). This was a good initial
    approach but after a couple of tests it was obvious that when a difference
    (something that was in A but not B) was found the SequenceMatcher got
    desynchronized and the rest of the A and B strings were also shown as
    different, even though they were the same but "shifted" by a couple of
    bytes (the size length of the initial difference).

    After detecting this I changed the algorithm to separate the input strings
    to this one, which takes advantage of the HTML format which is usually
    split by lines and organized by tabs:
        * \n
        * \r
        * \t

    And also uses tags and attributes:
        * <
        * '
        * "

    The single and double quotes will serve as separators for other HTTP
    response content types such as JSON.

    Splitting by <space> was an option, but I believe it would create multiple
    chunks without much meaning and reduce the performance improvement we
    have achieved.

    :param seq: A string
    :return: A list of strings (chunks) for the input string
    """
    chunks = []
    chunk = ''

    for c in seq:
        if c in '\n\t\r"\'<':
            chunks.append(chunk)
            chunk = ''
        else:
            chunk += c

    chunks.append(chunk)

    return chunks

def relative_distance_boolean(a_str, b_str, threshold=0.6):
    """
    Indicates if the strings to compare are similar enough. This (optimized)
    function is equivalent to the expression:
        relative_distance(x, y) > threshold

    :param a_str: A string object
    :param b_str: A string object
    :param threshold: Float value indicating the expected "similarity". Must be
                      0 <= threshold <= 1.0
    :return: A boolean value
    """
    if threshold == 0:
        return True
    elif threshold == 1.0:
        return a_str == b_str

    # First we need b_str to be the longer of both
    if len(b_str) < len(a_str):
        a_str, b_str = b_str, a_str

    alen = len(a_str)
    blen = len(b_str)

    if blen == 0 or alen == 0:
        return alen == blen

    if blen == alen and a_str == b_str and threshold <= 1.0:
        return True

    if threshold > upper_bound_similarity(a_str, b_str):
        return False
    else:
        # Bad, we can't optimize anything here
        return threshold <= difflib.SequenceMatcher(None,
                                                    split_by_sep(a_str),
                                                    split_by_sep(b_str)).quick_ratio()

def upper_bound_similarity(a, b):
    return (2.0*len(a))/(len(a)+len(b))

def fuzzy_equal(a_str, b_str, threshold=0.6):
    """
    Indicates if the 'similarity' index between strings
    is *greater equal* than 'threshold'. See 'relative_distance_boolean'.
    """
    return relative_distance_boolean(a_str, b_str, threshold)

def assign(service, arg):
    if service == "www":
        arg = util.makeurl(arg)
        return True,arg

def audit(arg):
    arg_1 = arg
    arg_2 = arg[0:-1] + r'//'

    _,_,original_response,_,_ = hackhttp.http(arg_1)
    time.sleep(0.05)
    _, _,windows_response,_,_ = hackhttp.http(arg_2)

    if fuzzy_equal(original_response,
                   windows_response, 0.98):
        desc = 'Fingerprinted this host as a Microsoft Windows system.'
        os_str = 'windows'
    else:
        desc = 'Fingerprinted this host as a *nix system. Detection for' \
               ' this operating system is weak, "if not windows then' \
               ' linux".'
        os_str = 'unix'
    security_note(desc,os_str)


if __name__ == '__main__':
    from dummy import *

    u = "https://www.t00ls.net/"
    audit(u)

    # try:
    #     code, head, html, redirect_url, log = hackhttp.http(u)
    # except Exception,ex:
    #     print ex
    # print code,head,len(html),redirect_url
