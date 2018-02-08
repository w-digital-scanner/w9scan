import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="w9scan scanner")
    parser.add_argument("--update", help="update w9scan",action="store_true")
    parser.add_argument("--guide", help="w9scan to guide",action="store_true")
    # subparser = parser.add_subparsers()

    # scan: new a sacn
    # cms = subparser.add_parser("scan", help=u"scan a url")
    # cms.add_argument("url", help="target url")
    # cms.add_argument("-p","--plugin", help="target url")
    # cms.add_argument("--scanAllPort", help="target url")
    # cms.add_argument("-t","--thread", help="target url")
    # cms.add_argument("-d","--depth", help="target url")
    

    args = parser.parse_args()
    print args