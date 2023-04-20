import unittest
import pytest
# import sys
# from pathlib import Path
# sys.path[0] = str(Path(sys.path[0]).parent)
from finParser import parse

# You can run 
# 
#   python test_parser.py
# 
# To verify that all the test cases pass.


FV_TESTCASES = [
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the FV?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a present value of 100. What is the fv?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and pv = 100. What is the Future Value?",
    "Given rate = 0.05/12, nper = 10*12, pmt = -100, and pv = -.25. What is the future value?",
    "Given a rate of 0.05/12, 10*12 periods, $100 payments, and a pv of 100. What is the future value?",
    ]
PV_TESTCASES = [
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the PV?",
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the pv?",
    "Given a rate of 0.05/12, nper of 10*12, and pmt of -100. What is the Present Value?",
    "Given rate = 0.05/12, nper = 10*12, and pmt = -100. What is the present value?",
    ]
IRR_TESTCASES = [
    "Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the IRR?",
    "Given cash flows of [-250000, 100000, 150000, 200000, 250000, 300000]. What is the irr?",
    "Given cash flows = [-250000, 100000, 150000, 200000, 250000, 300000]. What is the Internal Rate of Return?",
    "Given cash flows of [-250000, 100000, 150000, 200000, 250000, 300000]. What is the internal rate of return?",
    ]
NPV_TESTCASES = [
    "Given a rate of 0.08 and cash flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given a rate of 8% and cash flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given rate = 8.21% and cash flows of [-100, 39, 59, 55, 20]. What is the NPV?",
    "Given rate = 8.00% and cash flows of [$-100, $39, $59, $55, $20]. What is the NPV?",
    "Given rate = 128% and cash flows of [-$100, $39, $59, $55, $20]. What is the NPV?",
    "Given rate = 0.08 and cash flows = [-100, 39, 59, 55, 20]. What is the npv?",
    "Given rate = 0.08 and cash flows = [-100, 39, 59, 55, 20]. What is the Net Present Value?",
    "Given rate = 18% and cash flows = [-100, 39, 59, 55, 20.25]. What is the net present value?"
    ]

class TestParser(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_fv_0(self):
        inputs, functionName = parse(FV_TESTCASES[0])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100', 'pv = 100'])
        self.assertEqual(functionName, "FV")

    def test_fv_1(self):
        inputs, functionName = parse(FV_TESTCASES[1])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100', 'pv = 100'])
        self.assertEqual(functionName, "FV")
    
    def test_fv_2(self):
        inputs, functionName = parse(FV_TESTCASES[2])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100', 'pv = 100'])
        self.assertEqual(functionName, "FV")

    def test_fv_3(self):
        inputs, functionName = parse(FV_TESTCASES[3])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100', 'pv = -0.25'])
        self.assertEqual(functionName, "FV")

    def test_fv_4(self):
        inputs, functionName = parse(FV_TESTCASES[4])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100', 'pv = 100'])
        self.assertEqual(functionName, "FV")
        
    def test_pv_0(self):
        inputs, functionName = parse(PV_TESTCASES[0])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100'])
        self.assertEqual(functionName, "PV")

    def test_pv_1(self):
        inputs, functionName = parse(PV_TESTCASES[1])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100'])
        self.assertEqual(functionName, "PV")

    def test_pv_2(self):
        inputs, functionName = parse(PV_TESTCASES[2])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100'])
        self.assertEqual(functionName, "PV")

    def test_pv_3(self):
        inputs, functionName = parse(PV_TESTCASES[3])

        self.assertEqual(inputs, ['r = 0.004166666666666667', 'nper = 120', 'pmt = -100'])
        self.assertEqual(functionName, "PV")

    def test_irr_0(self):
        inputs, functionName = parse(IRR_TESTCASES[0])

        self.assertEqual(inputs, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "IRR")

    def test_irr_1(self):
        inputs, functionName = parse(IRR_TESTCASES[1])

        self.assertEqual(inputs, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "IRR")

    def test_irr_2(self):
        inputs, functionName = parse(IRR_TESTCASES[2])

        self.assertEqual(inputs, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "IRR")

    def test_irr_3(self):
        inputs, functionName = parse(IRR_TESTCASES[3])

        self.assertEqual(inputs, ['cash_flows = [-250000, 100000, 150000, 200000, 250000, 300000]'])
        self.assertEqual(functionName, "IRR")

    def test_npv_0(self):
        inputs, functionName = parse(NPV_TESTCASES[0])

        self.assertEqual(inputs, ['r = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_1(self):
        inputs, functionName = parse(NPV_TESTCASES[1])

        self.assertEqual(inputs, ['r = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_2(self):
        inputs, functionName = parse(NPV_TESTCASES[2])

        self.assertEqual(inputs, ['r = 0.0821', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_3(self):
        inputs, functionName = parse(NPV_TESTCASES[3])

        self.assertEqual(inputs, ['r = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_4(self):
        inputs, functionName = parse(NPV_TESTCASES[4])

        self.assertEqual(inputs, ['r = 1.28', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_5(self):
        inputs, functionName = parse(NPV_TESTCASES[5])

        self.assertEqual(inputs, ['r = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")

    def test_npv_6(self):
        inputs, functionName = parse(NPV_TESTCASES[6])

        self.assertEqual(inputs, ['r = 0.08', 'cash_flows = [-100, 39, 59, 55, 20]'])
        self.assertEqual(functionName, "NPV")
    
    def test_npv_7(self):
        inputs, functionName = parse(NPV_TESTCASES[7])

        self.assertEqual(inputs, ['r = 0.18', 'cash_flows = [-100, 39, 59, 55, 20.25]'])
        self.assertEqual(functionName, "NPV")

    def test_invalid_function(self):
        _, functionName = parse("Given r = 0.08 and pv = 100. What is the ABC?")
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "Error: No valid function name found. Allowed function names include: NPV, FV, IRR, and PV.\n")
        self.assertEqual(functionName, "Invalid Function Name") 

    def test_invalid_inputs(self):
        inputs, _ = parse("Given xqc = 123 and valid=456. What is the NPV?")
        out,_ = self.capsys.readouterr()
        INPUT_ERROR = "Error: Invalid input name found. Allowed inputs include rate, nper, pmt, pv, fv, and cash flows.\n"

        self.assertEqual(out, INPUT_ERROR*2)
        # TODO: I think this should do some break error instead of trying to call the evaluator with this
        self.assertEqual(inputs, ["ERROR: Invalid input.", "ERROR: Invalid input."]) 


if __name__ == "__main__":
    unittest.main()
