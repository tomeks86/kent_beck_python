#!/usr/bin/python

class TestCase:

	def __init__(self, name):
		self.name = name

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def run(self):
		self.setUp()
		method = getattr(self, self.name)
		method()
		self.tearDown()


class WasRun(TestCase):

	def __init__(self, name):
		self.wasRun = None
		TestCase.__init__(self, name)
		#super().__init__(name)

	def testMethod(self):
		self.wasRun = 1
		self.log += "testMethod "

	def setUp(self):
		self.wasRun = None
		self.wasSetUp = 1
		self.log = "setUp "

	def tearDown(self):
		self.log += "tearDown "


class TestCaseTest(TestCase):

	def setUp(self):
		self.test = WasRun("testMethod")

	def testRunning(self):
		assert(not self.test.wasRun)
		self.test.run()
		assert(self.test.wasRun)

	def testSetUp(self):
		self.test.run()
		assert(self.test.wasSetUp)

	def testSetUp(self):
		self.test.run()
		assert("setUp testMethod tearDown " == self.test.log)

	def testTemplateMethod(self):
		self.test.run()
		assert("setUp testMethod tearDown " == self.test.log)


TestCaseTest("testSetUp").run()
TestCaseTest("testRunning").run()
TestCaseTest("testTemplateMethod").run()
