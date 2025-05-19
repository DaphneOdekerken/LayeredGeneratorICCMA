## Use of argumentation theories in practice by the Dutch police
This generator generates ASPIC+ argumentation theories that are similar in 
structure to the argumentation theory that models the domain knowledge 
concerning fraud intake at the Dutch police. This use case is described in [2].
Note that, in this use case, the argumentation theory is not used for the 
"static" problem of acceptance (or listing extensions), but for the "dynamic" 
problems of stability and relevance.

## Properties of generated ASPIC+ argumentation theories
The generator uses generators from PyArg to generate ASPIC+ argumentation 
theories.
Properties of the ASPIC+ argumentation theories:
- Layered structure: rules go from knowledge to "topic" literals. 
- The highest layer is 4, so the path from argument premise to conclusion 
  can contain at most 4 defeasible rules.
- Contrariness by classical negation: each literal in the language has 
  exactly one contradictory --- its negation.
- No strict rules, just defeasible rules.
- No ordinary premises, just axioms.
- No preference ordering on the defeasible rules.
- No undercutters.
- All rules have 1, 2, 3, 4 or 5 antecedents.

## Conversion into abstract argumentation frameworks
Any ASPIC+ argumentation theory can be converted into an abstract 
argumentation framework. We do this by listing all arguments inferred by 
the argumentation theory and identifying all (rebuttal) attacks between 
those arguments.
Some properties of the resulting AFs:
- Long chains of attacks are impossible.
- For any attack (A,B) either A is an axiom or A is attacked by B itself or 
  another argument (which is a subargument of B).

## Conversion into ABA frameworks
Alternatively, the ASPIC+ argumentation framework can be converted into an 
ABA framework. For this, we use the method from Section 7 of [1].
Some properties of the resulting ABA frameworks:
- If the ASPIC+ framework had _l_ literals, then the ABA framework has 4 * 
  _l_ atoms (because the ASPIC+ framework with _l_ literals is created with 
  1.5 * _l_ rules and ABA introduces two new atoms for every ASPIC+ rule).
- If the ASPIC+ framework had _r_ rules, then the ABA framework has 2 * _r_ 
  rules.
- The ABA framework is flat: no assumption is the conclusion of a rule.

## Example usage
To install dependencies, run 
```commandline
pip install -r requirements.txt
```
This installs PyArg.

The benchmarks can then be generated using the following command.
```commandline
python .\console.py 50 3 ".\generated" "aba"
```
The first argument (50) refers to the number of literals for the ASPIC+ 
argumentation theory or theories.
The second argument (3) represents the number of instances that should be 
created. 
The third argument (".\generated") refers to the folder where the generated 
instances should be placed. 
The fourth argument ("aba") specifies the output format, which can be "aba" 
or "af".

## References
1. Heyninck, Jesse and Christian Strasser. "Relations between 
assumption-based approaches in nonmonotonic logic and formal argumentation."
16th International Workshop on Non-Monotonic Reasoning. 2016.
2. Odekerken, Daphne, et al. "Approximating stability for applied 
argument-based inquiry." 
Intelligent Systems with Applications 16 (2022): 200110.
