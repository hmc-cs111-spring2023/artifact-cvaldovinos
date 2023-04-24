import unittest
from numpy_financial import npv, irr, fv, pv
import pytest
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent / "src")
from evaluator import evaluate
from finParser import parse

# You can run 
# 
#   python test_evaluator.py
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

class TestEvaluator(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def capsys(self, capsys):
        self.capsys = capsys

    def test_fv_0(self):
        inputs, functionName = parse(FV_TESTCASES[0])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, fv(0.004166666666666667, 120, -100, 100))

    def test_fv_1(self):
        inputs, functionName = parse(FV_TESTCASES[1])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, fv(0.004166666666666667, 120, -100, 100))
    
    def test_fv_2(self):
        inputs, functionName = parse(FV_TESTCASES[2])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, fv(0.004166666666666667, 120, -100, 100))

    def test_fv_3(self):
        inputs, functionName = parse(FV_TESTCASES[3])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, fv(0.004166666666666667, 120, -100, -0.25))

    def test_fv_4(self):
        inputs, functionName = parse(FV_TESTCASES[4])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, fv(0.004166666666666667, 120, -100, 100))
        
    def test_pv_0(self):
        inputs, functionName = parse(PV_TESTCASES[0])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, pv(0.004166666666666667, 120, -100))

    def test_pv_1(self):
        inputs, functionName = parse(PV_TESTCASES[1])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, pv(0.004166666666666667, 120, -100))

    def test_pv_2(self):
        inputs, functionName = parse(PV_TESTCASES[2])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, pv(0.004166666666666667, 120, -100))

    def test_pv_3(self):
        inputs, functionName = parse(PV_TESTCASES[3])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, pv(0.004166666666666667, 120, -100))

    def test_irr_0(self):
        inputs, functionName = parse(IRR_TESTCASES[0])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, irr([-250000, 100000, 150000, 200000, 250000, 300000]))

    def test_irr_1(self):
        inputs, functionName = parse(IRR_TESTCASES[1])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, irr([-250000, 100000, 150000, 200000, 250000, 300000]))

    def test_irr_2(self):
        inputs, functionName = parse(IRR_TESTCASES[2])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, irr([-250000, 100000, 150000, 200000, 250000, 300000]))

    def test_irr_3(self):
        inputs, functionName = parse(IRR_TESTCASES[3])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, irr([-250000, 100000, 150000, 200000, 250000, 300000]))

    def test_npv_0(self):
        inputs, functionName = parse(NPV_TESTCASES[0])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.08, [-100, 39, 59, 55, 20]))

    def test_npv_1(self):
        inputs, functionName = parse(NPV_TESTCASES[1])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.08, [-100, 39, 59, 55, 20]))

    def test_npv_2(self):
        inputs, functionName = parse(NPV_TESTCASES[2])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.0821, [-100, 39, 59, 55, 20]))

    def test_npv_3(self):
        inputs, functionName = parse(NPV_TESTCASES[3])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.08, [-100, 39, 59, 55, 20]))

    def test_npv_4(self):
        inputs, functionName = parse(NPV_TESTCASES[4])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(1.28, [-100, 39, 59, 55, 20]))

    def test_npv_5(self):
        inputs, functionName = parse(NPV_TESTCASES[5])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.08, [-100, 39, 59, 55, 20]))

    def test_npv_6(self):
        inputs, functionName = parse(NPV_TESTCASES[6])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.08, [-100, 39, 59, 55, 20]))
    
    def test_npv_7(self):
        inputs, functionName = parse(NPV_TESTCASES[7])
        expectedValue = evaluate(functionName, inputs)

        self.assertEqual(expectedValue, npv(0.18, [-100, 39, 59, 55, 20.25]))

    def test_doubleRate_error(self):
        evaluate("", ["r = 0.01", "r = 0.01"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED A RATE, cannot assign two rates, please provide one.\n")

    def test_doubleCF_error(self):
        evaluate("", ["cash_flows = [-100, 200, 300]", "cash_flows = [-100, 200, 300]"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED CASH FLOWS, cannot assign two cash flows, please provide one.\n")

    def test_doublePV_error(self):
        evaluate("", ["pv = 100", "pv = 100"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED PRESENT VALUE, cannot assign two present values, please provide one.\n")

    def test_doubleFV_error(self):
        evaluate("", ["fv = 100", "fv = 100"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED FUTURE VALUE, cannot assign two future values, please provide one.\n")

    def test_doublePMT_error(self):
        evaluate("", ["pmt = 100", "pmt = 100"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED PAYMENT, cannot assign two payments, please provide one.\n")

    def test_doubleNPER_error(self):
        evaluate("", ["nper = 100", "nper = 100"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "YOU ALREADY ASSIGNED NUMBER OF PERIODS, cannot assign two number of periods, please provide one.\n")
    
    def test_invalidArg_error(self):
        evaluate("", ["invalid = 100"])
        out,_ = self.capsys.readouterr()

        self.assertEqual(out, "Invalid argument: " + "invalid = 100" + "\n The only valid arguments are: \n \n Rate - defines the rate and can be provided as: \n r = 0.07 or r = 7% or a rate of 2%, etc. \n Cash flows - defines the cash flows(TODO: these descriptions can likely be similar to those of google sheets/excel) and can be provided as:\n")


if __name__ == "__main__":
    unittest.main()
