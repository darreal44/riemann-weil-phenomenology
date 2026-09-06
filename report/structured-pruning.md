# Structured pruning

Unstructured: zero
individual weights.
Sparse GEMM, little
wall-clock gain on a
GPU unless N:M tensor
cores fire.

Structured: delete a
*block* that the
hardware already
understands.

    unit          what disappears
    filter/out    a conv channel
    neuron        a row+column of
                  a linear
    head          one attention
                  head (Q,K,V,O)
    layer/block   a whole
                  Transformer
                  block (depth)
    expert        one MoE expert
    N:M           N zeros in
                  every M weights
                  (2:4 Ampere)

Scores: ℓ2 of the
channel, activation
scale, Hessian /
OBC, gradient
sensitivity
(LLM-Pruner),
output similarity
of a head
(SlimLLM), NTK /
function-space
(NIRVANA). Then
usually a short
fine-tune.

Width vs depth
(2SSP): first drop
neurons in the FFN,
then drop whole
attention modules.
Allocation of
sparsity across
layers is half the
method.

Not drop-p: a head
is a subspace with
a hardware shape.
A Hecke prime is
a term in P. Same
word “drop”,
different lattice.
