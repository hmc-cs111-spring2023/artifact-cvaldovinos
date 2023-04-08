import unittest

from finParser import parse

# You can run 
# 
#   python test.py
# 
# To verify that all the test cases pass.


FV_TESTCASES = [
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the FV?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the fv?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the Future Value?",
    "Given rate = 0.05/12, nper = 10*12, pmt = -100, and pv = -100. What is the future value?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the future value?",
    ]
PV_TESTCASES = [
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the PV?",
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the pv?",
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the Present Value?",
    "Given rate = 0.05/12, nper = 10*12, and pmt = -100. What is the present value?",
    ]
IRR_TESTCASES = [
    "Given cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?",
    "Given cash_flows of [-250000, 100000, 150000, 200000, 250000, 300000]. What is the irr?",
    "Given cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the Internal Rate of Return?",
    "Given cash_flows of [-250000, 100000, 150000, 200000, 250000, 300000]. What is the internal rate of return?",
    ]
NPV_TESTCASES = [
    "Given a rate of 0.08 and cash_flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given a rate of 8% and cash_flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given rate = 8% and cash_flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given rate = 8% and cash_flows of [$-100, $39, $59, $55, $20]. What is the NPV?",
    "Given rate = 8% and cash_flows of [-$100, $39, $59, $55, $20]. What is the NPV?",
    "Given rate = 0.08 and cash_flows = [-100, 39, 59, 55, 20]. What is the npv?",
    "Given rate = 0.08 and cash_flows = [-100, 39, 59, 55, 20]. What is the Net Present Value?",
    "Given rate = 8% and cash_flows = [-100, 39, 59, 55, 20]. What is the net present value?"
    ]

class TestParser(unittest.TestCase):

    def test_fv_0(self):
        input, functionName = parse(FV_TESTCASES[0])

        self.assertEqual(input, ['a rate of 0.05/12', '10*12 periods', '$100 payments', 'a present value of 100'])
        self.assertEqual(functionName, "FV")

    def test_fv_1(self):
        input, functionName = parse(FV_TESTCASES[1])

        self.assertEqual(input, ['a rate of 0.05/12', '10*12 periods', '$100 payments', 'a present value of 100'])
        self.assertEqual(functionName, "fv")
    
    def test_fv_2(self):
        input, functionName = parse(FV_TESTCASES[2])

        self.assertEqual(input, ['a rate of 0.05/12', '10*12 periods', '$100 payments', 'a present value of 100'])
        self.assertEqual(functionName, "Future Value")

    def test_fv_3(self):
        input, functionName = parse(FV_TESTCASES[3])

        self.assertEqual(input, ['rate = 0.05/12', 'nper = 10*12', 'pmt = -100', 'pv = -100'])
        self.assertEqual(functionName, "future value")

    def test_fv_4(self):
        input, functionName = parse(FV_TESTCASES[4])

        self.assertEqual(input, ['a rate of 0.05/12', '10*12 periods', '$100 payments', 'a present value of 100'])
        self.assertEqual(functionName, "future value")
        
    def test_pv_0(self):
        input, functionName = parse(PV_TESTCASES[0])

        self.assertEqual(input, ['a rate of 0.05/12', 'nper of 10*12', 'pmt of -100'])
        self.assertEqual(functionName, "PV")

    def test_pv_1(self):
        input, functionName = parse(PV_TESTCASES[1])

        self.assertEqual(input, ['a rate of 0.05/12', 'nper of 10*12', 'pmt of -100'])
        self.assertEqual(functionName, "pv")

    def test_pv_2(self):
        input, functionName = parse(PV_TESTCASES[2])

        self.assertEqual(input, ['a rate of 0.05/12', 'nper of 10*12', 'pmt of -100'])
        self.assertEqual(functionName, "Present Value")

    def test_pv_3(self):
        input, functionName = parse(PV_TESTCASES[3])

        self.assertEqual(input, ['rate = 0.05/12', 'nper = 10*12', 'pmt = -100'])
        self.assertEqual(functionName, "present value")

    def test_irr_0(self):
        input, functionName = parse(IRR_TESTCASES[0])

        self.assertEqual(input, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "IRR")

    def test_irr_1(self):
        input, functionName = parse(IRR_TESTCASES[1])

        self.assertEqual(input, ['cash_flows of [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "irr")

    def test_irr_2(self):
        input, functionName = parse(IRR_TESTCASES[2])

        self.assertEqual(input, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "Internal Rate of Return")

    def test_irr_3(self):
        input, functionName = parse(IRR_TESTCASES[3])

        self.assertEqual(input, ['cash_flows of [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "internal rate of return")

    def test_npv_0(self):
        input, functionName = parse(NPV_TESTCASES[0])

        self.assertEqual(input, ['a rate of 0.08', 'cash_flows of [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_1(self):
        input, functionName = parse(NPV_TESTCASES[1])

        self.assertEqual(input, ['a rate of 8%', 'cash_flows of [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_2(self):
        input, functionName = parse(NPV_TESTCASES[2])

        self.assertEqual(input, ['rate = 8%', 'cash_flows of [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_3(self):
        input, functionName = parse(NPV_TESTCASES[3])

        self.assertEqual(input, ['rate = 8%', 'cash_flows of [$-100, $39, $59, $55, $20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_4(self):
        input, functionName = parse(NPV_TESTCASES[4])

        self.assertEqual(input, ['rate = 8%', 'cash_flows of [-$100, $39, $59, $55, $20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_5(self):
        input, functionName = parse(NPV_TESTCASES[5])

        self.assertEqual(input, ['rate = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "npv")

    def test_npv_6(self):
        input, functionName = parse(NPV_TESTCASES[6])

        self.assertEqual(input, ['rate = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "Net Present Value")
    
    def test_npv_7(self):
        input, functionName = parse(NPV_TESTCASES[7])

        self.assertEqual(input, ['rate = 8%', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "net present value")

if __name__ == "__main__":
    unittest.main()

