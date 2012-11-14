import json


class Casper(object):
    def __init__(self, options=None):
        defaults = {
            'viewportSize': {'width': 1024, 'height': 768}
        }
        if options is not None:
            defaults.update(options)
        self.js = ["var casper = require('casper').create(%s);" % json.dumps(defaults)]

    def start(self, url=None, action=None):
        self.url = 'null'
        if url is not None:
            self.url = "'%s'" % url
        self.js.append("casper.start(%s, function() {" % self.url)
        if action is not None:
            self.js.extend(action.js())
        self.js.append("});")

    def action(self, action):
        self.js.extend(action.js())

    def then(self, action):
        self.js.append("casper.then(function() {")
        self.js.extend(action.js())
        self.js.append("});")

    def run(self):
        self.js.append("casper.run();")

    def render(self):
        return '\n'.join(self.js)


class Capture(object):
    def __init__(self, filename):
        self.filename = filename

    def js(self):
        return ["this.capture('%s');" % self.filename]


class Open(object):
    def __init__(self, url, settings=None, action=None):
        self.url = url
        self.settings = {}
        if settings is not None:
            self.settings.update(settings)
        self._js = ["casper.open('%s', %s" % (self.url, json.dumps(settings), )]
        self._js.append(").then(function() {")
        if action is not None:
            self._js.extend(action.js())
        self._js.append("});")

    def js(self):
        return self._js