# FinMailAI Test Cases

## Core Functionality
| ID  | Description                          | Sample Input                              | Expected Output                     |
|-----|--------------------------------------|------------------------------------------|-------------------------------------|
| TC1 | Standard payment email               | `tests/emls/payment.eml`                 | `money_movement_outbound`           |
| TC2 | Trade finance with PDF attachment    | `tests/emls/trade_finance.eml`           | `trade_finance > letter_of_credit`  |

## Edge Cases
| ID  | Description                          | Test File                              | Verification Method               |
|-----|--------------------------------------|----------------------------------------|-----------------------------------|
| EC1 | Multi-page legal docs                | `edge_cases/legal_contract.zip`        | LayoutLMv3 parsing                |
| EC2 | Right-to-left amounts                | `edge_cases/arabic_payment.eml`        | Currency normalization            |