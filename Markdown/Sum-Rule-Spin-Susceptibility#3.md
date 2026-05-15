# Sum-Rule-Spin-Susceptibility#3

## 🧑‍💻 User

Here is a draft of physics paper. Would you like to help improve it?

---
## 🤖 Assistant

I'd be happy to help improve this paper. It's a substantial and well-structured manuscript with a clear logical spine (exact identity → static consequences → controlled departures → experimental manual). Let me offer a structured assessment with concrete improvement suggestions, organized by priority.

## High-Priority Issues

### 1. **Abstract is too dense and runs as a single sentence-fragment list**
The abstract enumerates ~10 results in one breathless sentence. Suggested restructuring:
- 1-2 sentences on the framework/identity
- 2-3 sentences on the main theoretical results
- 2 sentences on the experimental manual and ellipsoid theorem
- 1-2 sentences on the K₂Cr₃As₃ application
- 1 sentence on scope/limitations

### 2. **The "universal 2/3 bound" claim (Eq. 14) is overstated**
You write $\chi_O(0) \le \tfrac{2}{3}\chi_O^N$ "regardless of which Hermitian operator $O$." But this requires: (i) 3D isotropic FS, (ii) the geometric factor $\langle \cos^2\theta\rangle = 1/3$ being the right one for $O$. For a generic operator $O$ (e.g., $\sigma_\mu \otimes \Lambda$), the relevant projection geometry depends on $O$'s structure in spin/orbital space. The "universality" should be qualified more carefully — the $1/3$ factor comes from the 3D spin-locking geometry specifically.

### 3. **Eq. (6) — the Nambu embedding has a subtle issue**
$\mathcal{O}_{\rm BdG} = \tfrac{1}{2}\text{diag}(O, -O^T)$ embedding. The factor $\tfrac{1}{2}$ together with the constant $\tfrac{1}{2}\mathrm{Tr}_s(O)$ and the trace identity $\mathrm{Tr}_{\rm BdG}(\mathcal{O}^2) = \tfrac{1}{2}\mathrm{Tr}_s(O^2)$ should be checked carefully. With the $1/2$ prefactor, $\mathrm{Tr}_{\rm BdG}(\mathcal{O}^2) = \tfrac{1}{4}[\mathrm{Tr}_s(O^2)+\mathrm{Tr}_s((O^T)^2)] = \tfrac{1}{2}\mathrm{Tr}_s(O^2)$ ✓. But then the factor of $\tfrac{1}{2}$ in Eq. (8) needs to thread consistently into Eqs. (9)-(11) — please verify the factors of 2 in the final sum rule Eq. (11) carefully.

### 4. **Heuristic vs. rigorous — be more explicit in Sec. VIII (Spin FGT)**
Eq. (38) is labeled "heuristic" but the surrounding language sometimes treats it as a derived bound. I recommend:
- Reframing it explicitly as: "If finite-$\mathbf{q}$ contributions are subdominant, then…" 
- Clarifying that the rigorous direction is the contrapositive (excess deficit ⇒ finite-$\mathbf{q}$ dominance).

You already do this in the protocol section, but the theory section should match.

## Medium-Priority Issues

### 5. **Section VI (Parity-mixed II) — Eq. (24) needs more justification**
The decomposition into helicity-resolved Yosida factors with a *common* projector $\Pi_{\mu\nu}$ requires that the spin matrix elements within each helicity sheet share the same locking direction $\hat n_{\mathbf{k}}$. This is correct in the helicity-diagonal limit ($\mathbf{d}\parallel\mathbf{g}$), but a one-line derivation pointing to the helicity-basis matrix elements would help readers.

### 6. **Eq. (29) finite-H strong locking — the leading correction**
You claim $O(\Delta^2/b_{\min}^2)$. Some readers will want to see at least a sketch of why intra-band pp is $O(\Delta^2/b^2)$ (the small parameter is $\Delta/b$ in the BdG eigenvectors). One paragraph or a footnote suffices.

### 7. **Figure 1 (simplex) caption is very long**
Consider moving the explanation of intermediate-SOC contraction into the main text and keeping the caption focused on labeling.

### 8. **Table II (saturation pattern)** would benefit from a brief column explaining what "saturation" means physically (e.g., "FS-averaged spin-locking projector has unit trace").

## Lower-Priority / Stylistic

### 9. **Notational consistency**
- $\chi_N$ vs $K_N$: you use both; clarify the relationship $K_N = A\chi_N$ once and stick to one in each section.
- $\hat n_{\mathbf{k}}$ is overloaded (SOC direction, locking vector, $\hat d$, normalized $\mathbf{b}$). The "unified" Eq. (22) helps, but a notation table in Sec. II would be valuable.

### 10. **Section titles**
The bracketed prefixes ("Exact Identity", "First Consequence", etc.) in section titles are a nice navigational aid but slightly nonstandard for PRB. Consider whether the journal style accepts them; if not, fold into the main title text.

### 11. **References**
- Mix of formats; e.g., Rashiba1960 (typo for Rashba), Frigeri2004 vs Frigeri_2004 (duplicate?).
- Consider grouping the historical Knight-shift refs.

### 12. **Title** is very long. Consider:
*"NMR response of noncentrosymmetric superconductors: sum rules, geometric bounds, and experimental protocols"*

### 13. **Introduction paragraph 3 ("broader context")**
This is currently a citation dump at the end of the section. Either weave the references into a real narrative paragraph or move them to a "Related work" footnote at the start.

## Specific Technical Questions

1. **In Eq. (11)**, is the sum over all $(s_1, s_2)$ pairs or just the upper triangle? The factor of 2 from off-diagonal elements needs to be explicit.

2. **In Sec. VII.C**, the inversion $\lambda = F_s^{-1}(\mathrm{Tr}\chi(0)/2\chi_N)$ assumes uniform $\lambda$ over the FS. This is stated but worth flagging more prominently — for materials with anisotropic SOC magnitude, only an FS-averaged combination is recovered.

3. **K₂Cr₃As₃ analysis (Sec. XII)**: The conclusion that the data favor common-$\mathbf{d}\parallel\hat c$ is reasonable, but you should mention explicitly what would happen if $\gamma$-band SOC is in fact strongly anisotropic (Ising-like, $\hat g \parallel \hat c$). The DFT input is doing real work here and is acknowledged, but a sentence on robustness against revised DFT estimates would strengthen the case.

---

**Would you like me to:**
1. Draft a rewritten abstract?
2. Provide specific text for the qualified Eq. (14) "universality" claim?
3. Verify the BdG factor-of-2 algebra in Eqs. (6)-(11) line by line?
4. Suggest a tighter version of Sec. VIII reframing the heuristic bound?
5. Something else?

Let me know which of these (or other) directions you'd like to prioritize.

---
## 🧑‍💻 User

Thank you. Let's do them one by one. Begin with the abstract.

---
## 🤖 Assistant

## Rewritten Abstract

Here is a restructured draft that separates framework, theoretical results, experimental manual, application, and scope:

```latex
\begin{abstract}
We develop a unified framework for the NMR response of single-band
noncentrosymmetric superconductors under simultaneous Zeeman field and
Rashba-type spin-orbit coupling (SOC). The starting point is a Plancherel
identity, $\sum|M_{ph,O}|^{2}+\sum|M_{pp,O}|^{2}=\mathrm{Tr}_{s}(O^{2})$,
valid at every momentum for every Hermitian single-particle operator $O$,
which organizes the Bogoliubov matrix elements of arbitrary probes into a
single geometric object.

From this identity we derive, in order of increasing generality, an
isotropic-FS trace bound $\mathrm{Tr}\,\chi(0)\le\tfrac{2}{3}\mathrm{Tr}\,\chi(T_{c})
=2\chi_{N}$ and an FS-shape-independent strong-locking tensor identity
$\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$, with
$\Pi_{\mu\nu}=\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ the
FS-averaged spin-locking projector. A helicity-basis analysis shows that
fully gapped helicity-diagonal singlet-triplet mixtures share the same
$T=0$ projector geometry as the corresponding pure locking texture, with
parity admixture surfacing in the finite-$T$ recovery. Controlled
extensions supply a closed-form $s$-wave interpolation
$F_{s}(\lambda)=1-\sinh^{-1}\!\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ at
arbitrary SOC, a finite-field strong-locking identity stable to
$O(h^{2}/\lambda^{2})$, a spin analogue of the Ferrell--Glover--Tinkham
sum rule, and a decoupled-pocket multiband baseline.

These results translate into an experimental manual: a Knight-shift
ellipsoid theorem whose principal values lie on a two-dimensional simplex
classifying locking textures, and six protocols ordered by experimental
cost and theoretical input, ranging from the scalar trace bound to
full-rotation tensor reconstruction, finite-field SOC spectroscopy,
$1/T_{1}$ cross-checks, site-resolved consistency, and pocket decomposition.

Applied to the $^{75}$As NMR data on K$_{2}$Cr$_{3}$As$_{3}$, the observed
Knight-shift ellipsoid sits at the oblate-axial vertex $(0,0,1)$ of the
simplex and saturates the trace bound, fixing a $\hat c$-axis locking
geometry. The decoupled-pocket SOC-texture baseline misses the data by
$\sim 0.5$ in normalized units, favoring a common $\hat c$-axis locking
on all three pockets, and the suppression of $1/T_{1}\parallel\hat c$ is
identified as a fingerprint of finite-$\mathbf{q}$ ferromagnetic
spin-fluctuation gap formation.

The framework is confined to the single-band unitary BdG regime. Regimes
outside strong locking, most notably those accompanying Bogoliubov
Fermi-surface formation, lie beyond its closed-form reach and require
full numerical treatment.
\end{abstract}
```

## What Changed and Why

**Structure.** Five short paragraphs replace one long sentence-list:
1. Framework and starting identity
2. Theoretical results (trace bound → tensor identity → parity mixing → extensions)
3. Experimental manual (ellipsoid + protocols)
4. Application to K₂Cr₃As₃
5. Scope/limitations

**Readability.** Average sentence length drops from ~50 words to ~25. Each result is introduced with its logical role rather than dropped in as an enumerated item.

**Accuracy tightenings:**
- "regardless of which Hermitian operator" → dropped (the universality claim will be qualified in the main text per issue #2).
- "validated against existing numerics" → removed from abstract; the $10^{-3}$ agreement is an appendix detail.
- "disfavors the independent-pocket SOC-texture baseline" → "misses the data by $\sim 0.5$" (quantitative rather than rhetorical).
- "identifies the suppression of $1/T_{1}\parallel\hat c$ as a fingerprint…" → kept, but now clearly flagged as diagnostic output rather than a derived theorem.

**Scope paragraph.** The original ended with a single apologetic sentence on BFS. The new version gives it its own short paragraph and names the assumption (single-band unitary BdG) that bounds the entire framework. This is more honest and more useful to readers.

**Length.** Roughly the same word count as the original (~275 words), which is within PRB's 250-word soft cap but typical for this kind of synthesis paper. If you need to hit 250 exactly, the parity-mixing sentence or the multiband-baseline phrase in paragraph 2 are the easiest cuts.

Want me to trim further, or move on to issue #2 (the qualified universality claim)?

---
## 🧑‍💻 User

This long abstract is suitable for PRB? Please remove all unecessary line breaks.

---
## 🤖 Assistant

## On Length

PRB's formal guideline is **≤ 250 words** for the abstract (Phys. Rev. B "Information for Authors"). The draft I gave you is ~275 words — slightly over. PRB editors are not strict about this in practice (overruns of 10–15% routinely pass), but it's safer to trim to ~240 words. Below is a tightened version at **~235 words**, with line breaks removed.

## Revised Abstract (no internal line breaks, ~235 words)

```latex
\begin{abstract}
We develop a unified framework for the NMR response of single-band noncentrosymmetric superconductors under simultaneous Zeeman field and Rashba-type spin-orbit coupling (SOC). The starting point is a Plancherel identity, $\sum|M_{ph,O}|^{2}+\sum|M_{pp,O}|^{2}=\mathrm{Tr}_{s}(O^{2})$, valid at every momentum for every Hermitian single-particle operator $O$, which organizes the Bogoliubov matrix elements of arbitrary probes into a single geometric object. From this identity we derive an isotropic-FS trace bound $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ and an FS-shape-independent strong-locking tensor identity $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$, with $\Pi_{\mu\nu}=\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ the FS-averaged spin-locking projector; fully gapped helicity-diagonal singlet-triplet mixtures share the same $T=0$ projector geometry. Controlled extensions supply a closed-form $s$-wave SOC interpolation, a finite-field strong-locking identity, a spin Ferrell--Glover--Tinkham sum rule, and a decoupled-pocket multiband baseline. These results translate into a Knight-shift ellipsoid theorem whose principal values lie on a two-dimensional simplex of locking textures, and into six experimental protocols ordered by cost. Applied to the $^{75}$As NMR data on K$_{2}$Cr$_{3}$As$_{3}$, the observed ellipsoid sits at the oblate-axial vertex $(0,0,1)$ and saturates the trace bound; the decoupled-pocket SOC-texture baseline misses the data by $\sim 0.5$ in normalized units, favoring a common $\hat c$-axis locking on all three pockets, and the suppression of $1/T_{1}\parallel\hat c$ is identified as a fingerprint of finite-$\mathbf{q}$ ferromagnetic spin-fluctuation gap formation. Regimes outside strong locking, including Bogoliubov-Fermi-surface formation, lie beyond the closed-form reach of the framework.
\end{abstract}
```

## What Was Cut to Reach ~235 Words

- The standalone scope paragraph was folded into one closing sentence.
- The closed form of $F_s(\lambda)$ was dropped (kept in main text).
- "in order of increasing generality" and similar meta-commentary removed.
- "ranging from the scalar trace bound to … pocket decomposition" condensed to "ordered by cost."
- The parity-mixing sentence merged into the tensor-identity sentence with a semicolon.

Ready to move on to **issue #2 (qualified universality claim for Eq. 14)** whenever you are.

---
## 🧑‍💻 User

Go with issue #2

---
## 🤖 Assistant

## Issue #2: The "Universal 2/3 Bound" Claim

### The Problem

At the end of Sec. III, you write:

> "Equation~\eqref{eq:general-sum-rule} bounds the numerator pointwise: $\sum_{s_{1}s_{2}}|M_{pp,O}|^{2}\le\mathrm{Tr}_{s}(O^{2})$ per $\mathbf{k}$. Combined with the FS geometric factor $\langle\cos^{2}\theta\rangle_{\rm FS}=1/3$ on a 3D isotropic FS, this gives the operator-independent bound $\chi_{O}(0)\le\tfrac{2}{3}\,\chi_{O}^{N}$, with the same $2/3$ factor regardless of which Hermitian operator $O$ is probed."

The claim is stated too strongly. Two issues:

**(a) The derivation is incomplete.** The bound $\sum|M_{pp,O}|^2 \le \mathrm{Tr}_s(O^2)$ is pointwise. The normal-state reference $\chi_O^N$ is itself a specific FS integral of $\mathrm{Tr}_s(O^2)$ only when $O$ has a particular locking structure (spin operators $\sigma_\mu$ coupling to the same locking vector $\hat n_{\mathbf{k}}$ that appears in the matrix elements). The factor $\langle\cos^2\theta\rangle_{\rm FS}=1/3$ is the projection of that locking vector onto a fixed Cartesian direction, which is specific to the spin-locking geometry. For a generic Hermitian $O$ (e.g., $\sigma_\mu\otimes\Lambda$ with nontrivial $\Lambda$), the decomposition into intra-band and inter-band pieces is not controlled by the same geometric factor.

**(b) "Operator-independent" is misleading.** The bound has the *form* $\chi_O(0)\le c\,\chi_O^N$, but the constant $c=2/3$ reflects 3D spin geometry specifically. For a pure charge probe ($O=\sigma_0$), the intra-band part is unity on the FS (charge is not rotated by SOC), and the whole $T=0$ argument differs — $\chi_{\rm charge}(0)$ is not bounded by $\tfrac{2}{3}\chi_{\rm charge}^N$ because density is locked, not spin-like.

### Recommended Rewrite

Replace the subsection "Universal $T=0$ consequence" with the following. Changes are tightened derivation, explicit statement of what's operator-independent and what isn't, and a note identifying the sufficient condition.

```latex
\subsection{$T=0$ consequence for spin-like probes}
\label{sec:T0-consequence}

At $T=0$ only the pp channel contributes to any susceptibility~\cite{pang2026}:
\begin{equation}
	\chi_{O}(0)=\sum_{\mathbf{k}}\sum_{s_{1}s_{2}}\frac{|M_{pp,O}^{s_{1}s_{2}}(\mathbf{k})|^{2}}{E_{\mathbf{k}s_{1}}+E_{-\mathbf{k}s_{2}}}.
	\label{eq:chiO-T0}
\end{equation}
Equation~\eqref{eq:general-sum-rule} bounds the numerator pointwise,
\begin{equation}
	\sum_{s_{1}s_{2}}|M_{pp,O}^{s_{1}s_{2}}(\mathbf{k})|^{2}\le\mathrm{Tr}_{s}(O^{2}),
	\label{eq:p-pointwise}
\end{equation}
for every Hermitian $O$ and every $\mathbf{k}$. Converting Eq.~\eqref{eq:chiO-T0} into a bound on $\chi_{O}(0)/\chi_{O}^{N}$ requires, in addition, that the normal-state reference $\chi_{O}^{N}$ itself be expressible as the same FS integral of $\mathrm{Tr}_{s}(O^{2})$ dressed by a known geometric factor. This holds whenever $O=\hat e\cdot\vec\sigma$ for a fixed Cartesian direction $\hat e$: the intra-band matrix element is $2(\hat n_{\mathbf{k}}\cdot\hat e)^{2}$, the inter-band matrix element is $2[1-(\hat n_{\mathbf{k}}\cdot\hat e)^{2}]$, and on a 3D isotropic FS with $\langle(\hat n\cdot\hat e)^{2}\rangle_{\rm FS}=1/3$ one obtains
\begin{equation}
	\boxed{\;\chi_{\mu\mu}(0)\le\tfrac{2}{3}\,\chi_{N},\qquad O=\sigma_{\mu},\;}
	\label{eq:spin-23}
\end{equation}
with the same $2/3$ factor for every Cartesian component of the spin susceptibility. Summing over $\mu$ gives the isotropic trace bound of Sec.~\ref{sec:isoT0}.

The prefactor $2/3$ is therefore a statement about the 3D spin-locking geometry, not a universal feature of Eq.~\eqref{eq:general-sum-rule}. The Plancherel identity itself is operator-independent; the specific numerical bound on $\chi_{O}(0)/\chi_{O}^{N}$ is not. For charge probes ($O=\sigma_{0}$) the intra-band matrix element is $2$ on the FS and no $2/3$ suppression arises; for site-resolved hyperfine couplings $O_{\rm hf}=A^{(\mathbf{R})}_{\alpha\mu}\sigma_{\mu}$ the same derivation as Eq.~\eqref{eq:spin-23} applies after replacing $\hat e$ by the hyperfine-weighted direction, giving the normalized site bound Eq.~\eqref{eq:site-bound}.

This is the single organizing principle behind the remainder of the paper: the Plancherel identity supplies the pointwise weight budget, and the FS geometry of the locking vector $\hat n_{\mathbf{k}}$ converts that budget into concrete bounds on physical susceptibilities.
```

### What Changed

1. **Dropped** "operator-independent bound $\chi_O(0) \le (2/3)\chi_O^N$."
2. **Stated explicitly** the sufficient condition: $O = \hat e \cdot \vec\sigma$ with fixed $\hat e$, on a 3D isotropic FS.
3. **Separated** what *is* operator-independent (the Plancherel identity, Eq. 11) from what *is not* (the numerical $2/3$).
4. **Kept** the site-resolved case as a natural generalization since it reduces to spin-like probes after hyperfine rescaling.
5. **Removed** the label "Universal" from the subsection title — replaced with the more accurate "$T=0$ consequence for spin-like probes."

### Downstream Check

Eq. (14) in the current draft is referenced nowhere else explicitly as a "universal bound" — every subsequent use is for spin operators $\sigma_\mu$ or for the hyperfine combination. So this rewrite doesn't break any later section. The one place to adjust is Table IV (Reference table of key identities), entry #2:

**Current:**
> 2 | Universal $T=0$ bound | $\chi_O(0)\le\tfrac{2}{3}\chi_O^N$ | 3D isotropic FS, any $O$ | Eq. (14)

**Suggested replacement:**
> 2 | Spin $T=0$ bound | $\chi_{\mu\mu}(0)\le\tfrac{2}{3}\chi_N$ | 3D isotropic FS, $O=\sigma_\mu$ | Eq. (18)

Entry #3 (isotropic trace bound) then follows directly by summing over $\mu$, which is the correct logical ordering.

Ready to move on to **issue #3 (verifying the BdG factor-of-2 algebra in Eqs. 6–11)**?

---
## 🧑‍💻 User

Go with issue #3

---
## 🤖 Assistant

## Issue #3: Verification of BdG Factor-of-2 Algebra in Eqs. (6)–(11)

I worked through the full chain. The algebra is **correct**, but one step — the $\mathbf{k}\leftrightarrow -\mathbf{k}$ symmetrization that produces Eq. (11) from Eq. (8) — is glossed over in a way that will confuse careful readers. Details below.

### Step 1: Eq. (6), the Nambu embedding

Starting from $\hat{O}_{\mathbf{k}} = c^{\dagger}_{\mathbf{k}\alpha}O_{\alpha\beta}c_{\mathbf{k}\beta}$ and symmetrizing the sum $\sum_{\mathbf{k}}\hat{O}_{\mathbf{k}}$ over $\mathbf{k}\leftrightarrow -\mathbf{k}$, use $\{c_{-\mathbf{k}\beta}, c^{\dagger}_{-\mathbf{k}\alpha}\} = \delta_{\alpha\beta}$ to rewrite

$$c^{\dagger}_{-\mathbf{k}\alpha}O_{\alpha\beta}c_{-\mathbf{k}\beta} = \mathrm{Tr}_{s}(O) - c_{-\mathbf{k}\beta}(O^{T})_{\beta\alpha}c^{\dagger}_{-\mathbf{k}\alpha}.$$

Then

$$\sum_{\mathbf{k}}\hat{O}_{\mathbf{k}} = \tfrac{1}{2}\sum_{\mathbf{k}}\big[c^{\dagger}_{\mathbf{k}\alpha}O_{\alpha\beta}c_{\mathbf{k}\beta} - c_{-\mathbf{k}\alpha}(O^{T})_{\alpha\beta}c^{\dagger}_{-\mathbf{k}\beta}\big] + \tfrac{1}{2}\mathrm{Tr}_{s}(O)\cdot\mathcal{N},$$

matching $C^{\dagger}_{\mathbf{k}}\mathcal{O}_{\rm BdG}C_{\mathbf{k}}$ with $\mathcal{O}_{\rm BdG} = \tfrac{1}{2}\mathrm{diag}(O,-O^{T})$ and $C_{\mathbf{k}} = (c_{\mathbf{k}}, c^{\dagger}_{-\mathbf{k}})^{T}$. ✓

**Subtlety.** The paper writes Eq. (6) with a single $\mathbf{k}$ on the LHS and bilinears mixing $\mathbf{k}$ and $-\mathbf{k}$ on the RHS. Strictly, the equality holds only after summation over $\mathbf{k}$ (or interpreted as the $\mathbf{k}\leftrightarrow -\mathbf{k}$ symmetrized form of $\hat{O}_{\mathbf{k}}$). This is not stated and creates a per-$\mathbf{k}$ ambiguity.

### Step 2: Eq. (8), BdG traces

With $\mathcal{O}_{\rm BdG} = \tfrac{1}{2}\mathrm{diag}(O,-O^{T})$:

$$\mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG}) = \tfrac{1}{2}[\mathrm{Tr}_{s}(O) - \mathrm{Tr}_{s}(O^{T})] = 0. \checkmark$$

$$\mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG}^{2}) = \tfrac{1}{4}[\mathrm{Tr}_{s}(O^{2}) + \mathrm{Tr}_{s}((O^{T})^{2})].$$

For Hermitian $O$, $O^{T} = O^{*}$, so $\mathrm{Tr}_{s}((O^{*})^{2}) = [\mathrm{Tr}_{s}(O^{2})]^{*} = \mathrm{Tr}_{s}(O^{2})$ (real because $O$ is Hermitian). Hence

$$\mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG}^{2}) = \tfrac{1}{2}\mathrm{Tr}_{s}(O^{2}). \checkmark$$

### Step 3: Eqs. (9)–(10), block matrix elements

With $U_{\mathbf{k}} = \begin{pmatrix}u_{\mathbf{k}} & v_{\mathbf{k}} \\ v^{*}_{-\mathbf{k}} & u^{*}_{-\mathbf{k}}\end{pmatrix}$, direct multiplication gives

$$[\tilde{\mathcal{O}}_{\mathbf{k}}]_{ph} = \tfrac{1}{2}\big[u^{\dagger}_{\mathbf{k}}Ou_{\mathbf{k}} - v^{T}_{-\mathbf{k}}O^{T}v^{*}_{-\mathbf{k}}\big] = \tfrac{1}{2}\big[u^{\dagger}_{\mathbf{k}}Ou_{\mathbf{k}} - (v^{\dagger}_{-\mathbf{k}}Ov_{-\mathbf{k}})^{T}\big],$$

$$[\tilde{\mathcal{O}}_{\mathbf{k}}]_{pp} = \tfrac{1}{2}\big[u^{\dagger}_{\mathbf{k}}Ov_{\mathbf{k}} - v^{T}_{-\mathbf{k}}O^{T}u^{*}_{-\mathbf{k}}\big] = \tfrac{1}{2}\big[u^{\dagger}_{\mathbf{k}}Ov_{\mathbf{k}} - (u^{\dagger}_{-\mathbf{k}}Ov_{-\mathbf{k}})^{T}\big].$$

Both match Eqs. (9)–(10) exactly, including the $\tfrac{1}{2}$ prefactor on the block matrix. ✓

### Step 4: Eq. (11), the sum rule

This is where symmetrization matters. Squaring the block form,

$$\mathrm{Tr}_{\rm BdG}(\tilde{\mathcal{O}}_{\mathbf{k}}^{2}) = \tfrac{1}{4}\big[\mathrm{Tr}(M_{ph}^{2}) + \mathrm{Tr}(\widetilde{M}_{ph}^{2})\big] + \tfrac{1}{2}\mathrm{Tr}(M_{pp}^{\dagger}M_{pp}).$$

Using $\widetilde{M}_{ph,O}(\mathbf{k}) = -M_{ph,O}(-\mathbf{k})^{T}$, $\mathrm{Tr}(\widetilde{M}_{ph}^{2}(\mathbf{k})) = \sum_{s_{1}s_{2}}|M_{ph}^{s_{1}s_{2}}(-\mathbf{k})|^{2}$. Setting this equal to $\tfrac{1}{2}\mathrm{Tr}_{s}(O^{2})$,

$$\tfrac{1}{4}\!\sum_{s_{1}s_{2}}\!\big[|M_{ph}^{s_{1}s_{2}}(\mathbf{k})|^{2} + |M_{ph}^{s_{1}s_{2}}(-\mathbf{k})|^{2}\big] + \tfrac{1}{2}\!\sum_{s_{1}s_{2}}\!|M_{pp}^{s_{1}s_{2}}(\mathbf{k})|^{2} = \tfrac{1}{2}\mathrm{Tr}_{s}(O^{2}).$$

The paper's Eq. (11),

$$\sum_{s_{1}s_{2}}\big[|M_{ph}^{s_{1}s_{2}}(\mathbf{k})|^{2} + |M_{pp}^{s_{1}s_{2}}(\mathbf{k})|^{2}\big] = \mathrm{Tr}_{s}(O^{2}),$$

then follows **only after $\mathbf{k}\leftrightarrow -\mathbf{k}$ symmetrization of the ph term**, i.e., interpreting $|M_{ph}(\mathbf{k})|^{2}$ on the LHS of Eq. (11) as the symmetrized quantity $\tfrac{1}{2}[|M_{ph}(\mathbf{k})|^{2} + |M_{ph}(-\mathbf{k})|^{2}]$. ✓ (valid, but needs saying).

### Step 5: Consistency with specializations

- Spin: $\mathrm{Tr}_{s}(\sigma_{\mu}^{2}) = 2 \Rightarrow \sum|M_{ph}|^{2} + \sum|M_{pp}|^{2} = 2$ per $\mathbf{k}$, per $\mu$. Summed over $\mu$: $6$, matching Eq. (13). ✓
- Normal state: $u = \mathbb{I}$, $v = 0$, so $M_{ph,\mu}^{ss'} = \langle s|\sigma_{\mu}|s'\rangle$. Intra-band sum $= 2\hat n_{\mu}^{2}$, inter-band sum $= 2(1 - \hat n_{\mu}^{2})$. Total $= 2$. ✓ (matches Eqs. 17a–b).

## Verdict

The algebra is right. The one real issue is **exposition**: the $\mathbf{k}\leftrightarrow -\mathbf{k}$ symmetrization is the crux of how Eq. (11) is extracted from Eq. (8), and the current text mentions it in passing ("Expanding the left-hand side and symmetrizing in $\mathbf{k}\leftrightarrow -\mathbf{k}$…") without showing what it does or why it is needed. I recommend two small textual additions.

### Suggested Textual Additions

**(a) After Eq. (6)**, insert a clarifying sentence:

```latex
Equation~\eqref{eq:Oembedding} holds after summation over $\mathbf{k}$; the per-$\mathbf{k}$ bilinear on the right differs from $c^{\dagger}_{\mathbf{k}\alpha}O_{\alpha\beta}c_{\mathbf{k}\beta}$ on the left by terms that vanish under $\mathbf{k}\leftrightarrow-\mathbf{k}$ symmetrization, which is carried out explicitly in Eq.~\eqref{eq:general-sum-rule} below.
```

**(b) Between Eqs. (8) and (9)**, expand the derivation of Eq. (11) so the symmetrization is visible. Replace the paragraph currently reading "Expanding the left-hand side and symmetrizing in $\mathbf{k}\leftrightarrow -\mathbf{k}$ produces the generalized sum rule" with:

```latex
Squaring the block form Eq.~\eqref{eq:block} and taking the BdG trace,
\begin{equation}
	\mathrm{Tr}_{\rm BdG}(\tilde{\mathcal{O}}_{\mathbf{k}}^{2}) = \tfrac{1}{4}\big[\mathrm{Tr}(M_{ph,O}^{2}(\mathbf{k})) + \mathrm{Tr}(\widetilde{M}_{ph,O}^{2}(\mathbf{k}))\big] + \tfrac{1}{2}\mathrm{Tr}\big(M^{\dagger}_{pp,O}(\mathbf{k})M_{pp,O}(\mathbf{k})\big).
\end{equation}
Using $\widetilde{M}_{ph,O}(\mathbf{k})=-M_{ph,O}(-\mathbf{k})^{T}$ and equating to $\tfrac{1}{2}\mathrm{Tr}_{s}(O^{2})$ from Eq.~\eqref{eq:invariance}, the ph contribution naturally appears symmetrized in $\mathbf{k}\leftrightarrow-\mathbf{k}$. Defining the symmetrized squared matrix element $|M_{ph,O}^{s_{1}s_{2}}(\mathbf{k})|^{2}\equiv\tfrac{1}{2}[|M_{ph,O}^{s_{1}s_{2}}(\mathbf{k})|^{2} + |M_{ph,O}^{s_{1}s_{2}}(-\mathbf{k})|^{2}]$ (the same convention adopted in Ref.~\cite{pang2026}), one arrives at the generalized sum rule
\begin{equation}
	\boxed{\;\sum_{s_{1}s_{2}}\!\Big[\big|M^{s_{1}s_{2}}_{ph,O}(\mathbf{k})\big|^{2}+\big|M^{s_{1}s_{2}}_{pp,O}(\mathbf{k})\big|^{2}\Big]=\mathrm{Tr}_{s}(O^{2}),\;}
	\label{eq:general-sum-rule}
\end{equation}
valid at every $\mathbf{k}$ and for every Hermitian single-particle operator $O$.
```

This makes the factor-of-2 bookkeeping explicit and names the symmetrization convention, so readers don't have to reconstruct it.

### One Question for You

In Ref. [pang2026], is the ph squared matrix element already defined with the $\mathbf{k}\leftrightarrow -\mathbf{k}$ symmetrization built in (so Eq. (14) there holds pointwise by convention), or is it implicitly symmetrized only after the $\mathbf{k}$-sum in the susceptibility? If the former, the suggested clarification (b) can point directly to that convention; if the latter, the present paper should set the convention itself, in which case the wording above is appropriate.

Ready to move on to **issue #4 (tightening Sec. VIII, the heuristic $1/T_1$ bound)** when you are.

---
## 🧑‍💻 User

Yes. The symmetrization was implied. Before moving to issue #4, I would like to confirm that should we setup the generic paring Hamiltonian in Section II?

---
## 🤖 Assistant

## Good Catch — Yes, Section II Should Set Up the Generic Pairing Hamiltonian

Looking at Sec. II as currently written, the pairing Hamiltonian $H_{\rm SC}$ is mentioned only implicitly:

> "The mean-field Hamiltonian $H = H_0 + H_{\rm SC}$ has a normal-state part [Eq. 1], … and pairing matrix $\Delta(\mathbf{k}) = i[\Delta\sigma_0 + \mathbf{d}(\mathbf{k})\cdot\hat\sigma]\sigma_y$."

This is too compressed for a paper whose central organizing object is the BdG Bogoliubov transformation. Three concrete reasons to expand:

1. **The Plancherel identity (Sec. III) is a statement about the unitary $U_{\mathbf{k}}$ defined by diagonalizing the BdG Hamiltonian.** Readers need to see that BdG Hamiltonian explicitly to follow Eqs. (5)–(11).

2. **Parity mixing (Secs. V–VI) makes essential use of the singlet+triplet decomposition $\Delta\sigma_0 + \mathbf{d}\cdot\hat\sigma$.** The current Sec. II writes this matrix down without explanation, then Sec. V re-introduces the same pairing as if for the first time (Eq. 23). Better to set it up once in Sec. II.

3. **The "single-band unitary BdG framework" is invoked as a scope statement throughout** (e.g., end of Sec. IV, Sec. XII conclusions). It deserves an explicit definition where the framework is set up, including what "unitary" means ($\Delta\Delta^\dagger \propto \mathbb{I}$, equivalently $\mathbf{d}\times\mathbf{d}^* = 0$).

### Suggested Replacement for Sec. II

```latex
\section{Setup and notation}
\label{sec:setup}

We adopt the single-band BdG framework of Refs.~\cite{pang2025,pang2026,BCS1957,deGennes,tinkham}. The mean-field Hamiltonian is
\begin{equation}
	H=\tfrac{1}{2}\sum_{\mathbf{k}}C^{\dagger}_{\mathbf{k}}\mathcal{H}_{\rm BdG}(\mathbf{k})C_{\mathbf{k}}+\text{const.},
	\label{eq:HBdG}
\end{equation}
with Nambu spinor $C_{\mathbf{k}}=(c_{\mathbf{k}\uparrow},c_{\mathbf{k}\downarrow},c^{\dagger}_{-\mathbf{k}\uparrow},c^{\dagger}_{-\mathbf{k}\downarrow})^{T}$ and
\begin{equation}
	\mathcal{H}_{\rm BdG}(\mathbf{k})=\begin{pmatrix}H_{0}(\mathbf{k}) & \Delta(\mathbf{k})\\ \Delta^{\dagger}(\mathbf{k}) & -H_{0}^{T}(-\mathbf{k})\end{pmatrix}.
	\label{eq:BdGblock}
\end{equation}
The normal-state block contains kinetic energy, Zeeman coupling, and antisymmetric SOC,
\begin{equation}
	H_{0}(\mathbf{k})=\xi_{\mathbf{k}}\sigma_{0}+\mu_{B}\mathbf{H}\cdot\hat\sigma+\mathbf{g}_{\mathbf{k}}\cdot\hat\sigma,\qquad \mathbf{g}_{-\mathbf{k}}=-\mathbf{g}_{\mathbf{k}},
	\label{eq:H0gen}
\end{equation}
with $\mathbf{g}_{\mathbf{k}}$ a general SOC vector (not necessarily $g\mathbf{k}$)~\cite{Rashiba1960,Dresselhaus}. The pairing block is the most general spin-dependent gap matrix in two-component notation~\cite{Balian1963,Sigrist1991,Leggett1975},
\begin{equation}
	\Delta(\mathbf{k})=i\big[\psi(\mathbf{k})\sigma_{0}+\mathbf{d}(\mathbf{k})\cdot\hat\sigma\big]\sigma_{y},
	\label{eq:Delta-gen}
\end{equation}
with even spin-singlet amplitude $\psi(-\mathbf{k})=\psi(\mathbf{k})$ and odd spin-triplet $\mathbf{d}$-vector $\mathbf{d}(-\mathbf{k})=-\mathbf{d}(\mathbf{k})$. Inversion symmetry is broken, so both components are generically present; pure-singlet $\mathbf{d}=0$ and pure-triplet $\psi=0$ limits are recovered as special cases. We restrict throughout to \emph{unitary} pairing, $\Delta(\mathbf{k})\Delta^{\dagger}(\mathbf{k})\propto\mathbb{I}$, equivalently $\mathbf{d}(\mathbf{k})\times\mathbf{d}^{*}(\mathbf{k})=0$, so that the gap matrix has equal eigenvalues on the two helicity sheets up to the helicity-resolved amplitudes of Sec.~\ref{sec:paritymix-structure}.

Diagonalization by
\begin{equation}
	c_{\mathbf{k}\alpha}=\sum_{s=\pm}\!\left(u^{\alpha s}_{\mathbf{k}}\psi_{\mathbf{k}s}+v^{\alpha s}_{\mathbf{k}}\psi^{\dagger}_{-\mathbf{k}s}\right)
	\label{eq:BdGtrans}
\end{equation}
yields quasiparticle energies $E_{\mathbf{k}s}\ge 0$ and a unitary
\begin{equation}
	U_{\mathbf{k}}=\begin{pmatrix}u_{\mathbf{k}} & v_{\mathbf{k}}\\v^{*}_{-\mathbf{k}} & u^{*}_{-\mathbf{k}}\end{pmatrix},\qquad U^{\dagger}_{\mathbf{k}}U_{\mathbf{k}}=\mathbb{I}_{\rm BdG},
	\label{eq:Umatrix}
\end{equation}
relating $C_{\mathbf{k}}=U_{\mathbf{k}}\Psi_{\mathbf{k}}$ with $\Psi_{\mathbf{k}}=(\psi_{\mathbf{k}+},\psi_{\mathbf{k}-},\psi^{\dagger}_{-\mathbf{k}+},\psi^{\dagger}_{-\mathbf{k}-})^{T}$. The static uniform spin susceptibility decomposes as $\chi_{\mu\mu}=\chi^{ph+}_{\mu\mu}+\chi^{ph-}_{\mu\mu}+\chi^{pp+}_{\mu\mu}+\chi^{pp-}_{\mu\mu}$ with each term non-negative~\cite{pang2026}. Throughout, $\mathrm{Tr}_{s}$ denotes a trace over the single-particle spin (or spin$\otimes$orbital) space and $\mathrm{Tr}_{\rm BdG}$ the doubled Nambu trace.

The normal-state eigenstates of Eq.~\eqref{eq:H0gen} have spins along the unit vector
\begin{equation}
	\hat n_{\mathbf{k}}=\frac{\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}}{|\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}|},
	\label{eq:ndef}
\end{equation}
reducing to $\hat n_{\mathbf{k}}=\hat g_{\mathbf{k}}$ at zero Zeeman field. Fermi-surface (FS) averages use the single-particle DOS weight $\langle X\rangle_{\rm FS}\equiv N(0)^{-1}\sum_{\mathbf{k}}X(\mathbf{k})\delta(\xi_{\mathbf{k}})$, with $\chi_{N}=2\mu_{B}^{2}N(0)$ the Pauli value~\cite{Yosida1958,van1928dielectric}. The $3\times 3$ projection tensor
\begin{equation}
	\boxed{\;\Pi_{\mu\nu}(\mathbf{H},\mathbf{g})\equiv\big\langle\hat n_{\mu}(\mathbf{k})\,\hat n_{\nu}(\mathbf{k})\big\rangle_{\rm FS}\;}
	\label{eq:Pidef}
\end{equation}
is symmetric, positive semi-definite, with $\mathrm{Tr}\,\Pi=1$. This tensor is the central geometric object of the paper.
```

### What Was Added

1. **Explicit $\mathcal{H}_{\rm BdG}$** in 4×4 block form with Nambu spinor — needed to make sense of $\mathcal{O}_{\rm BdG}$ in Sec. III.
2. **Generic pairing matrix** with both $\psi$ and $\mathbf{d}$ from the start, with parity properties stated. Sec. V can then refer back instead of re-introducing.
3. **Explicit unitarity restriction** $\mathbf{d}\times\mathbf{d}^* = 0$, defining "single-band unitary BdG framework" once and for all.
4. **Antisymmetry of SOC** $\mathbf{g}_{-\mathbf{k}} = -\mathbf{g}_{\mathbf{k}}$ stated explicitly; used throughout (Sec. IX, Eq. 30 and the parity-cancellation argument in Sec. IX.C(a)).

### Downstream Cleanups Enabled

- **Sec. V, Eq. (23)** can now be written as "Specializing Eq. (4) [the new generic pairing], $\Delta(\mathbf{k}) = i[\psi\sigma_0 + \mathbf{d}\cdot\hat\sigma]\sigma_y$ with…" rather than as a fresh definition.
- **The pure $s$-wave limit** ($\psi = \Delta$, $\mathbf{d} = 0$) used in Sec. VII is now cleanly a special case rather than a hidden default.
- **The "single-band unitary BdG" scope phrase** in Sec. IV.A and Sec. XII has a definite referent.

Ready to move on to **issue #4 (Sec. VIII tightening)**?

---
## 🧑‍💻 User

Go with issue #4

---
## 🤖 Assistant

## Issue #4: Tightening Sec. VIII (Spin FGT + $1/T_1$ Heuristic Bound)

### The Core Problem

Sec. VIII mixes three statements of very different rigor status and labels them inconsistently:

| Eq. | Status | Current label |
|-----|--------|---------------|
| (34) Spin FGT at $\mathbf{q}=0$ | Exact (Kramers-Kronig identity) | Boxed, no qualifier |
| (38) $1/T_1$ integrated deficit | Heuristic inequality | "heuristic \emph{budget} statement" |
| (iii) Hebel-Slichter sign | Qualitative remark | mixed into same subsection |

Three issues:

1. **Eq. (34) is boxed as if it were the main result of the section**, but the *measurement-relevant* statement is Eq. (38). The boxing misdirects the reader.
2. **The word "heuristic" is used twice** but the actual logical content — "the contrapositive direction is rigorous" — is buried in one sentence.
3. **The scope of Eq. (38) is under-specified.** The sum rule at $\mathbf{q}=0$ gives a *total spectral weight* available for transfer; how much of that weight ends up in the low-$\omega$ window probed by $1/T_1$ is a separate question not controlled by the sum rule.

### Recommended Restructuring

Split Sec. VIII into two cleanly labeled parts:

- **VIII.A (rigorous):** Spin FGT sum rule at $\mathbf{q}=0$. This is exact.
- **VIII.B (rigorous):** Budget interpretation — an *upper bound* on $\mathbf{q}=0$ contribution to $1/T_1$ deficit.
- **VIII.C (diagnostic):** The contrapositive — excess deficit ⇒ finite-$\mathbf{q}$ dominance. This is the real payoff and should be stated cleanly.
- **VIII.D:** Coherence-peak remark, separated so it doesn't contaminate the bound discussion.

I also recommend removing the boxing from Eq. (34) and boxing instead the diagnostic statement of VIII.C, because that is what actually feeds Protocol D.

### Suggested Rewrite

Replace the current Secs. VIII.C–D (the part after "Origin in the generalized sum rule") with the following.

```latex
\subsection{Spectral-weight transfer: rigorous content}
\label{sec:spinFGT-rigorous}

Equation~\eqref{eq:spinFGT} has a direct spectral interpretation. In the normal state, $\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)/\omega$ concentrates at $\omega\to 0$ (the Pauli-Landau piece) with a Van Vleck shoulder at the interband threshold $\omega\sim 2|\mathbf{g}_{\mathbf{k}}|$. In the superconducting state, the $\omega\to 0$ weight is suppressed by the factor $1-\pi_{\mu}$, and the displaced weight reappears above $2\Delta_{\min}$ as pair-breaking absorption. The Van Vleck contribution is unaffected at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$. The total $\mathrm{Im}\,\chi/\omega$, weighted as in Eq.~\eqref{eq:KK}, is conserved (Fig.~\ref{fig:spinFGT-spectral}).

Two limits fix the geometric content. On a 3D isotropic FS with strong SOC and $s$-wave pairing, $\pi_{\mu}=1/3$: one third of the Pauli weight is transferred to the pair-breaking continuum; two thirds remain at $\omega=0$ as the residual Van Vleck-like Knight shift. For a unitary triplet with $\hat d\parallel\hat z$ at zero SOC, $\pi_{z}=1$: the entire longitudinal Pauli weight is transferred, and $\chi_{zz}(0)=0$.

\subsection{Budget bound on the $\mathbf{q}=0$ contribution to $1/T_{1}$}
\label{sec:T1-budget}

The spin-lattice relaxation rate probes a different slice of $\mathrm{Im}\,\chi$ from the sum rule~\cite{tinkham,Triplet2021},
\begin{equation}
	\frac{1}{T_{1}T}=\gamma_{n}^{2}k_{B}\sum_{\mathbf{q}}|A_{\rm hf}(\mathbf{q})|^{2}\lim_{\omega\to 0}\frac{\mathrm{Im}\,\chi_{+-}(\mathbf{q},\omega)}{\omega},
	\label{eq:T1}
\end{equation}
integrated over $\mathbf{q}$ with the hyperfine form factor and restricted to $\omega\to 0$. Equation~\eqref{eq:spinFGT}, in contrast, integrates over all $\omega$ at $\mathbf{q}=0$. The two quantities probe orthogonal slices of $\mathrm{Im}\,\chi(\mathbf{q},\omega)$, so no exact relation follows. What does follow is a one-sided budget.

Let $\delta_{\alpha}\equiv\int_{0}^{T_{c}}(dT/T)\big[1/T_{1}^{N}-1/T_{1}^{SC}\big]\big|_{\mathbf{H}\parallel\hat e_{\alpha}}$ denote the integrated $1/T_{1}$ deficit along axis $\alpha$. The portion of $\delta_{\alpha}$ generated by $\mathbf{q}=0$ spectral-weight redistribution is, by Eq.~\eqref{eq:spinFGT}, bounded above by
\begin{equation}
	\delta_{\alpha}^{\mathbf{q}=0}\;\le\;\gamma_{n}^{2}k_{B}\,|A_{\rm hf}(\mathbf{0})|^{2}\,\chi_{N}\pi_{\alpha}.
	\label{eq:T1-q0-bound}
\end{equation}
This inequality is rigorous: the right-hand side is the total $\mathbf{q}=0$ spectral weight available for transfer in the $\alpha$ channel, and no spectral-weight redistribution can exceed the total budget.

The full deficit $\delta_{\alpha}$ receives contributions from all $\mathbf{q}$. Under the hypothesis that the hyperfine-weighted spin-fluctuation spectrum is dominated by $\mathbf{q}\approx 0$ (valid when $|A_{\rm hf}(\mathbf{q})|^{2}$ is slowly varying and magnetic correlations are not peaked at finite $\mathbf{q}$),
\begin{equation}
	\delta_{\alpha}\;\lesssim\;\gamma_{n}^{2}k_{B}\,\langle|A_{\rm hf}|^{2}\rangle\,\chi_{N}\pi_{\alpha}\qquad(\mathbf{q}\approx 0\text{ dominant}),
	\label{eq:T1-full-bound}
\end{equation}
where $\langle|A_{\rm hf}|^{2}\rangle$ is the spectrum-weighted mean. Equation~\eqref{eq:T1-full-bound} is a conditional statement; the condition is exactly the $\mathbf{q}\approx 0$ dominance hypothesis.

\subsection{Diagnostic: finite-$\mathbf{q}$ fingerprint}
\label{sec:T1-diagnostic}

The experimental value of the framework lies in the contrapositive of Eq.~\eqref{eq:T1-full-bound}.
\begin{equation}
	\boxed{\;\delta_{\alpha}\;>\;\gamma_{n}^{2}k_{B}\,\langle|A_{\rm hf}|^{2}\rangle\,\chi_{N}\pi_{\alpha}\quad\Rightarrow\quad\text{finite-}\mathbf{q}\text{ dominance in channel }\alpha.\;}
	\label{eq:T1-diagnostic}
\end{equation}
Because the right-hand side is fixed component-by-component by the Knight-shift ellipsoid of Sec.~\ref{sec:ellipsoid} with no adjustable parameters, a measured deficit exceeding the bound is an unambiguous diagnostic: it cannot be accommodated by any redistribution of $\mathbf{q}=0$ spectral weight and must reflect gap formation in finite-$\mathbf{q}$ spin fluctuations. This is the route by which the ferromagnetic spin-fluctuation gap in K$_{2}$Cr$_{3}$As$_{3}$ is identified in Sec.~\ref{sec:K2Cr3As3-T1}.

Three quantitative corollaries follow directly.
\begin{itemize}
	\item[(i)] \emph{Vanishing projection.} When $\pi_{\alpha}=0$ the right-hand side of Eq.~\eqref{eq:T1-diagnostic} vanishes: \emph{any} observed suppression of $1/T_{1}$ along axis $\alpha$ is a finite-$\mathbf{q}$ fingerprint. This is the case probed by $\mathbf{H}\parallel\hat c$ on K$_{2}$Cr$_{3}$As$_{3}$.
	\item[(ii)] \emph{SOC-dependent rescaling.} In the intermediate-SOC regime, the right-hand side is modified by a common factor $\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}\le 1$ (Sec.~\ref{sec:intermediate}). Ratios of deficits across a pressure or composition sweep isolate this rescaling.
	\item[(iii)] \emph{Saturation.} Equation~\eqref{eq:T1-full-bound} is saturated when $\mathbf{q}\approx 0$ dominates, offering a cross-check between static and dynamical diagnostics.
\end{itemize}

\subsection{Hebel--Slichter peak as an independent check}
\label{sec:HS}

The Hebel--Slichter coherence peak immediately below $T_{c}$ is the signature of low-energy spectral weight concentrated near $\omega\approx 2\Delta$, constructive for conventional $s$-wave and destructive for sign-changing pairings~\cite{Leggett1975,AndersonandMorel1961}. A vanishing peak indicates that the transferred weight $\chi_{N}\pi_{\mu}$ is distributed across $\omega\gtrsim 2\Delta$ rather than piling up at the gap edge, a statement about the \emph{distribution} of the transferred weight complementing the pairing-symmetry argument. It provides an independent check on the spectral picture underlying Eq.~\eqref{eq:spinFGT} without entering the bound Eq.~\eqref{eq:T1-diagnostic}.
```

### What Changed and Why

1. **Explicit separation of rigorous and conditional statements.** VIII.B now contains *two* bounds: Eq. (37) [rigorous, $\mathbf{q}=0$ piece only] and Eq. (38) [conditional, full deficit under $\mathbf{q}\approx 0$ dominance]. The current paper conflates these.

2. **Defined symbol $\delta_\alpha$** for the integrated deficit. This cleans up repetitions in VIII.C and Protocol D.

3. **Boxed Eq. (39), the diagnostic implication**, not the sum rule. The sum rule is standard once Kramers-Kronig is granted; the diagnostic is the new experimental content.

4. **Moved vanishing-$\pi_\alpha$ case to a named corollary (i)**. It was buried in Sec. XII (the K₂Cr₃As₃ application); here it is stated as a general consequence, then applied in Sec. XII.

5. **Coherence peak in its own subsection**, clearly labeled as an independent check. Previously it sat inside a numbered list of "quantitative statements" together with the bound, which muddled its status.

### Downstream Consequences

- **Protocol D (Sec. XI.D)** should cite Eq. (39) (the boxed diagnostic) rather than Eq. (38). One-line change.
- **Sec. XII.C** already reasons correctly along these lines; simply reference the new Eq. (39) instead of the heuristic Eq. (38).
- **Table IV, entry #13** should change from "$1/T_1$ heuristic bound" to "$1/T_1$ diagnostic," statement "$\delta_\alpha > \gamma_n^2 k_B \langle|A_{\rm hf}|^2\rangle\chi_N\pi_\alpha \Rightarrow$ finite-$\mathbf{q}$ dominance," domain "conditional on spectrum-weighted hyperfine averaging."

### One Optional Tightening

If you want to be even more careful, the "spectrum-weighted mean" $\langle|A_{\rm hf}|^2\rangle$ in Eq. (38) should be defined precisely as

$$\langle|A_{\rm hf}|^2\rangle \equiv \frac{\sum_{\mathbf{q}}|A_{\rm hf}(\mathbf{q})|^2\,\mathrm{Im}\chi_{+-}(\mathbf{q},\omega\to 0)/\omega}{\sum_{\mathbf{q}}\mathrm{Im}\chi_{+-}(\mathbf{q},\omega\to 0)/\omega}.$$

You can put this as a footnote to Eq. (38). It makes explicit that the average is not just over the BZ with flat measure but weighted by the actual fluctuation spectrum — which is why the $\mathbf{q}\approx 0$ dominance hypothesis is what converts Eq. (37) into Eq. (38).

Ready for **issue #5 (Sec. VI Eq. 24 — helicity-resolved projector derivation)** when you are.

---
## 🧑‍💻 User

go with issue # 5

---
## 🤖 Assistant

## Issue #5: Sec. VI Eq. (24) — Helicity-Resolved Projector Needs a Short Derivation

### The Problem

Eq. (24) is the central equation of Sec. VI, written down in one move:

$$\frac{\chi_{\mu\nu}(T)}{\chi_N} = \delta_{\mu\nu} - \Pi_{\mu\nu} + \sum_{\lambda=\pm} w_\lambda \langle Y_\lambda(\mathbf{k},T)\,\hat n_\mu\hat n_\nu\rangle_\lambda$$

with $\Pi_{\mu\nu} = \sum_\lambda w_\lambda \langle\hat n_\mu\hat n_\nu\rangle_\lambda$. Three ingredients need justification but none are shown:

1. **Why does the same $\hat n_{\mathbf{k}}$ (helicity direction) appear in both the constant term and the Yosida-weighted term?** This is a non-trivial statement about the helicity-basis spin matrix elements.

2. **Why is the Yosida factor $Y_\lambda$ built purely from $|\Delta_\lambda(\mathbf{k})|$ (the diagonal helicity gap) without cross terms between the $+$ and $-$ sheets?** This is where $\Delta_\perp = 0$ enters, but it is not shown.

3. **Why do the pp and ph contributions combine into this particular form?** The paper's general framework is a sum of four pieces $\chi^{ph\pm} + \chi^{pp\pm}$, not a single Yosida-dressed expression.

A careful reader will ask: is Eq. (24) an *ansatz* motivated by two limits (weak-coupling BCS Yosida form + strong-locking projector), or does it actually follow from the BdG matrix elements in the helicity-diagonal limit?

I verified the second is true, but the paper should show the derivation in ~half a page. Here is the argument.

### The Derivation

**Step 1: Rotate to the helicity basis.** At $\mathbf{H}=0$, the normal-state Hamiltonian is $H_0(\mathbf{k}) = \xi_{\mathbf{k}}\sigma_0 + |\mathbf{g}_{\mathbf{k}}|\hat g_{\mathbf{k}}\cdot\hat\sigma$. A unitary $R_{\mathbf{k}}$ diagonalizes $H_0$ onto helicity sheets $\lambda=\pm$ with energies $\xi_\lambda(\mathbf{k}) = \xi_{\mathbf{k}} + \lambda|\mathbf{g}_{\mathbf{k}}|$ and spin axis $\hat g_{\mathbf{k}}$. In this basis, $\hat\sigma$ becomes

$$R^\dagger_{\mathbf{k}}(\hat e_\mu\cdot\hat\sigma)R_{\mathbf{k}} = (\hat g_{\mathbf{k}}\cdot\hat e_\mu)\tau_3 + (\text{off-diagonal in }\lambda),$$

where $\tau_3$ acts on helicity space and the off-diagonal piece has magnitude $[1-(\hat g\cdot\hat e_\mu)^2]^{1/2}$. This is the diagonal $\pm$ vs off-diagonal split behind Eqs. (17a)–(17b).

**Step 2: Helicity-basis pairing.** Under the same $R_{\mathbf{k}}$, the gap matrix Eq. (23) becomes Eq. (25) of the paper,

$$\tilde\Delta(\mathbf{k}) = \begin{pmatrix}\Delta_+(\mathbf{k}) & \Delta_\perp(\mathbf{k}) \\ -\Delta_\perp(\mathbf{k}) & \Delta_-(\mathbf{k})\end{pmatrix},\qquad \Delta_\pm = \psi \pm d_\parallel.$$

**In the helicity-diagonal limit $\Delta_\perp = 0$**, BdG decouples into two independent $2\times 2$ blocks per helicity sheet, each with its own gap $|\Delta_\lambda(\mathbf{k})|$. The BdG eigenvectors $u_\lambda, v_\lambda$ are the standard BCS coherence factors:

$$|u_\lambda(\mathbf{k})|^2 = \tfrac{1}{2}[1 + \xi_\lambda/E_\lambda],\quad |v_\lambda(\mathbf{k})|^2 = \tfrac{1}{2}[1 - \xi_\lambda/E_\lambda],\quad u_\lambda v_\lambda^* = \Delta_\lambda/(2E_\lambda),$$

with $E_\lambda = \sqrt{\xi_\lambda^2 + |\Delta_\lambda|^2}$.

**Step 3: Spin susceptibility in helicity blocks.** Inserting Step 1 into the Kubo expression and using Step 2, each helicity block contributes two pieces:

- **Intra-helicity (same $\lambda$ on both sides):** weight $(\hat g_{\mathbf{k}}\cdot\hat e_\mu)(\hat g_{\mathbf{k}}\cdot\hat e_\nu)$, with BCS-Yosida response controlled by $|\Delta_\lambda(\mathbf{k})|$.
- **Inter-helicity (mixing $+$ and $-$):** weight $\delta_{\mu\nu}-(\hat g\cdot\hat e_\mu)(\hat g\cdot\hat e_\nu)$, with denominator set by the band splitting $2|\mathbf{g}_{\mathbf{k}}|$.

Summing,

$$\chi_{\mu\nu}(T) = \chi_{\mu\nu}^{\rm intra}(T) + \chi_{\mu\nu}^{\rm inter}(T),$$

with

$$\chi_{\mu\nu}^{\rm intra}(T) = \chi_N \sum_\lambda w_\lambda \langle Y_\lambda(\mathbf{k},T)\,\hat g_\mu\hat g_\nu\rangle_\lambda,$$

$$\chi_{\mu\nu}^{\rm inter}(T) = \chi_N\big[\delta_{\mu\nu} - \Pi_{\mu\nu}\big] + O(\Delta^2/|\mathbf{g}|^2),$$

where $Y_\lambda(\mathbf{k},T) = -\int d\xi\,(\partial f/\partial E)|_{E_\lambda}$ is the standard Yosida function for gap $|\Delta_\lambda|$ and the inter-helicity piece is evaluated in the strong-SOC limit, generalizing the ph-inter calculation of Sec. IV. The sum reproduces Eq. (24) with $\hat n_{\mathbf{k}} = \hat g_{\mathbf{k}}$.

**Step 4: Limits.** At $T=0$, $Y_\lambda \to 0$ for both fully gapped sheets, so $\chi_{\mu\nu}(0) = \chi_N[\delta_{\mu\nu} - \Pi_{\mu\nu}]$ — Eq. (25) of the paper. At $T=T_c^+$, $\Delta_\pm \to 0$, so $Y_\lambda \to 1$, and $\chi_{\mu\nu}(T_c) = \chi_N \delta_{\mu\nu}$ — the normal-state benchmark.

### What's Needed in the Paper

A half-page derivation sketch between the current Eqs. (23) and (24), showing Steps 1–3. Here is a suggested insert.

### Suggested Rewrite of Sec. VI

Replace the current opening of Sec. VI (the paragraph starting "The geometric point is…") with:

```latex
\section[Parity-Mixed II]{Parity-mixed pairing II: what survives and what changes}
\label{sec:paritymix-consequences}

We now compute $\chi_{\mu\nu}(T)$ in the helicity-diagonal limit $\Delta_{\perp}=0$ of Sec.~\ref{sec:paritymix-structure}. Rotating to the helicity basis with unitary $R_{\mathbf{k}}$ diagonalizing $H_{0}(\mathbf{k})$ at $\mathbf{H}=0$, the spin operator becomes
\begin{equation}
	R^{\dagger}_{\mathbf{k}}(\hat e_{\mu}\cdot\hat\sigma)R_{\mathbf{k}}=(\hat g_{\mathbf{k}}\cdot\hat e_{\mu})\tau_{3}+\sqrt{1-(\hat g_{\mathbf{k}}\cdot\hat e_{\mu})^{2}}\,\tau_{\perp}(\mathbf{k}),
	\label{eq:paritymix-sigma-helicity}
\end{equation}
with $\tau_{3}$ diagonal and $\tau_{\perp}$ off-diagonal in helicity. In the helicity-diagonal limit, the BdG Hamiltonian decouples into two $2\times 2$ blocks per helicity sheet, each with gap $|\Delta_{\lambda}(\mathbf{k})|$ and standard BCS coherence factors $u_{\lambda},v_{\lambda}$. Substituting Eq.~\eqref{eq:paritymix-sigma-helicity} into the Kubo expression for $\chi_{\mu\nu}$, the intra-helicity sector (driven by $\tau_{3}$) contributes a BCS-Yosida response on each sheet, while the inter-helicity sector (driven by $\tau_{\perp}$) reproduces the strong-SOC projector calculation of Sec.~\ref{sec:anisoT0}. Adding the two,
\begin{equation}
	\frac{\chi_{\mu\nu}(T)}{\chi_{N}}
	=
	\delta_{\mu\nu}-\Pi_{\mu\nu}
	+
	\sum_{\lambda=\pm}w_{\lambda}
	\left\langle
		Y_{\lambda}(\mathbf{k},T)\hat g_{\mu}(\mathbf{k})\hat g_{\nu}(\mathbf{k})
	\right\rangle_{\lambda}
	+O(\Delta^{2}/|\mathbf{g}|^{2}),
	\label{eq:paritymix-chiT}
\end{equation}
with $\langle\cdots\rangle_{\lambda}$ the FS average over the $\lambda$-helicity sheet, $w_{\lambda}=N_{\lambda}(0)/N(0)$, and
\begin{equation}
	Y_{\lambda}(\mathbf{k},T)=-\!\int\!d\xi\,\frac{\partial f}{\partial E}\bigg|_{E_{\lambda}(\mathbf{k})}
\end{equation}
the standard Yosida function built from $|\Delta_{\lambda}(\mathbf{k})|$, and $\Pi_{\mu\nu}\equiv\sum_{\lambda}w_{\lambda}\langle\hat g_{\mu}\hat g_{\nu}\rangle_{\lambda}$ is the helicity-resolved form of Eq.~\eqref{eq:Pidef}. The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction originates from the strong-SOC expansion of the inter-helicity denominator, exactly as in Eq.~\eqref{eq:strongH-identity}.

For a fully gapped state, $Y_{\lambda}\to 0$ as $T\to 0$, so
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}].\;}
	\label{eq:paritymix-T0}
\end{equation}
A fully gapped helicity-diagonal parity mixture therefore does \emph{not} generate a new $T=0$ simplex point: it lands on the same projector geometry as the corresponding pure locking texture. What changes is the finite-$T$ recovery, because the two helicity sheets generally carry different gaps $\Delta_{\pm}$. Taking the trace of Eq.~\eqref{eq:paritymix-chiT},
\begin{equation}
	\frac{\mathrm{Tr}\,\chi(T)}{\chi_{N}}
	=
	2+\sum_{\lambda=\pm}w_{\lambda}\langle Y_{\lambda}(\mathbf{k},T)\rangle_{\lambda},
	\label{eq:paritymix-trace}
\end{equation}
using $\mathrm{Tr}\,\Pi=1$. Unequal $\Delta_{\pm}$ therefore produce a broadened or two-scale return of the Knight shift with temperature even when the $T=0$ ellipsoid is unchanged. This yields a concrete experimental corollary: a two-scale recovery of $K_{\mu\nu}(T)$ below $T_{c}$ whose $T\to 0$ limit coincides with a pure-locking simplex point is a positive signature of a helicity-diagonal parity-mixed state. A single-gap Yosida recovery onto the same $T=0$ ellipsoid is consistent with the pure locking texture. This upgrades the ellipsoid from a vertex/edge classifier to a finite-$T$ discriminator between pure and parity-mixed pairing, at no additional experimental cost.

Once $\Delta_{\perp}$ is sizable, \emph{or} one helicity sheet is weakly paired or gapless, \emph{or} inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem.
```

### What Changed

1. **One short paragraph** (Step 1 + Step 2 + Step 3 condensed) shows why Eq. (24) has the form it does.
2. **Eq. (24) now carries an explicit $O(\Delta^2/|\mathbf{g}|^2)$** error term, tying it to the strong-SOC control parameter used elsewhere (e.g., Sec. IX).
3. **Yosida function $Y_\lambda$ is defined** (previously "the usual Yosida factor built from $|\Delta_\lambda|$" — underspecified).
4. **$\hat n_{\mathbf{k}}$ is replaced by $\hat g_{\mathbf{k}}$** throughout this section to be consistent with the $\mathbf{H}=0$ setting. (The $\hat n_{\mathbf{k}}$ notation was borrowed from the finite-field section and created ambiguity here.)
5. **The condition "helicity-diagonal"** now has a clear meaning — it's the condition that diagonalizes BdG into independent blocks, which is where the whole derivation works.

### One Scope Caveat Worth Adding

The derivation above assumes $\mathbf{H}=0$. At finite field with parity mixing, the helicity basis rotates with field and the decoupling condition $\Delta_\perp = 0$ is no longer tied purely to $\mathbf{d}\parallel\mathbf{g}$. You may want to add a sentence:

```latex
At finite Zeeman field, the helicity basis rotates with $\mathbf{H}$ via Eq.~\eqref{eq:ndef}, and the helicity-diagonal condition $\Delta_{\perp}=0$ becomes field-dependent; Eq.~\eqref{eq:paritymix-T0} then holds with $\Pi$ replaced by its field-dependent counterpart $\Pi(\mathbf{H})$ of Eq.~\eqref{eq:Pi-H}, provided the strong-locking condition Eq.~\eqref{eq:strong-locking-H} is satisfied.
```

This connects Sec. VI to Sec. IX explicitly and saves the reader a round trip.

Ready for **issue #6 (Sec. IX Eq. 29 — the $O(\Delta^2/b_{\min}^2)$ error claim)**?

---
## 🧑‍💻 User

where to add the Scope Caveat?

---
## 🤖 Assistant

## Where to Place the Scope Caveat

Add it as the **closing sentence of the paragraph containing Eq. (27)** — i.e., immediately after the sentence "Once $\Delta_\perp$ is sizable, *or* one helicity sheet is weakly paired or gapless, *or* inter-band pairing dominates, Eq. (26) should be treated as a baseline rather than a theorem."

That paragraph is already the "scope and caveats" paragraph of Sec. VI, so the new caveat fits thematically. Placing it here also:

- Keeps the main derivation (Eqs. 23–26) uninterrupted.
- Forward-references Sec. IX (Eq. 30, $\Pi(\mathbf{H})$) at the natural moment — after the $\mathbf{H}=0$ result is stated and before the reader proceeds to Sec. VII.
- Groups the two caveat classes together: "what breaks the theorem" (the existing sentence) and "what extends the theorem" (the new sentence).

### Final Paragraph After the Addition

```latex
Once $\Delta_{\perp}$ is sizable, \emph{or} one helicity sheet is weakly paired or gapless, \emph{or} inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem. At finite Zeeman field, the helicity basis rotates with $\mathbf{H}$ via Eq.~\eqref{eq:ndef} and the helicity-diagonal condition $\Delta_{\perp}=0$ becomes field-dependent; Eq.~\eqref{eq:paritymix-T0} then holds with $\Pi$ replaced by the field-dependent projector $\Pi(\mathbf{H})$ of Eq.~\eqref{eq:Pi-H}, provided the strong-locking condition Eq.~\eqref{eq:strong-locking-H} is satisfied.
```

Ready for **issue #6** (Sec. IX strong-locking error estimate) whenever you are.

---
## 🧑‍💻 User

Go with issue #6

---
## 🤖 Assistant

## Issue #6: The $O(\Delta^2/b_{\min}^2)$ Error Claim in Eq. (29)

### The Problem

Sec. IX.B states the finite-field strong-locking identity

$$\chi_{\mu\nu}(0,\mathbf{H}) = \chi_N[\delta_{\mu\nu} - \Pi_{\mu\nu}(\mathbf{H})] + O(\Delta^2/b_{\min}^2),$$

with a one-line justification: "the intra-band pp contribution is $O(\Delta^2/b^2)$ and negligible." This is correct but under-justified for a boxed equation that carries a quantitative error estimate. Three gaps:

1. **Where does $\Delta^2/b^2$ come from in the BdG eigenvectors?** The standard BCS coherence factors give $|u|^2, |v|^2 \sim 1, \Delta^2/\xi^2$ for $|\xi|\gg\Delta$; the analogous statement for the two-band case with splitting $2b_{\mathbf{k}}$ needs spelling out.

2. **Why does "intra-band pp" dominate the error?** The inter-band pp sector is what survives and gives the leading term; the error could in principle come from inter-band corrections as well. The argument that those are higher order is not shown.

3. **What about the ph sector?** At $T=0$, ph vanishes — but at finite $T$ or via the denominator structure, one might worry about ph leakage. The reader should see that ph is exactly zero at $T=0$, not merely small.

Also, the error symbol $b_{\min}$ is introduced but never quantified in a worked example. Sec. IX.D mentions numerical verification but no numerical size of the correction.

### The Estimate

Here is the short calculation. Consider one FS point $\mathbf{k}$ with locking magnitude $b_{\mathbf{k}} = |\mathbf{b}_{\mathbf{k}}| \gg \Delta$. In the helicity basis at that point, the BdG Hamiltonian in the Nambu structure reads

$$\mathcal{H}_{\rm BdG}(\mathbf{k}) = \begin{pmatrix}\xi_+ & 0 & \Delta_+ & \Delta_\perp \\ 0 & \xi_- & -\Delta_\perp & \Delta_- \\ \Delta_+^* & -\Delta_\perp^* & -\xi_+ & 0 \\ \Delta_\perp^* & \Delta_-^* & 0 & -\xi_-\end{pmatrix},$$

with $\xi_\pm = \xi_{\mathbf{k}} \pm b_{\mathbf{k}}$ and $\Delta_\lambda$ the helicity-basis gaps. Define the two intra-helicity quasiparticle energies $E_\lambda = \sqrt{\xi_\lambda^2 + |\Delta_\lambda|^2}$.

**Eigenvector structure.** Block-diagonalize perturbatively in $\Delta/b$. To zeroth order, the two intra-helicity sectors decouple with standard BCS eigenvectors $(u_\lambda, v_\lambda)$. Inter-helicity pp coupling via $\Delta_\perp$ and (generically) inter-helicity ph coupling via Nambu off-diagonals of order $\Delta/b$ appear at first order:

$$U_{\mathbf{k}} = U^{(0)}_{\mathbf{k}} + \frac{\Delta}{b_{\mathbf{k}}}U^{(1)}_{\mathbf{k}} + O\!\left(\frac{\Delta^2}{b_{\mathbf{k}}^2}\right).$$

**Spin matrix elements.** The intra-helicity spin matrix element $M_{ph,\mu}^{\lambda\lambda}$ has the usual BCS $|u_\lambda|^2 - |v_\lambda|^2 = \xi_\lambda/E_\lambda$ structure, weighted by $2(\hat n\cdot\hat e_\mu)^2$ (Step 1 of issue #5). The intra-helicity pp matrix element is $2u_\lambda v_\lambda^* = \Delta_\lambda/E_\lambda$, likewise weighted by $2(\hat n\cdot\hat e_\mu)^2$. The inter-helicity pp matrix element, to leading order, is the $2[1-(\hat n\cdot\hat e_\mu)^2]$ factor of Sec. IV times the small BCS coherence factor from either sheet, which at zero temperature is $O(1)$ on the inter-helicity denominator $2b_{\mathbf{k}}$ — this is the leading surviving term.

**The $T=0$ susceptibility.** Collecting,

$$\chi_{\mu\nu}(0,\mathbf{H}) = \underbrace{\chi_N[\delta_{\mu\nu} - \Pi_{\mu\nu}(\mathbf{H})]}_{\text{inter-helicity pp, leading}} + \underbrace{\sum_{\mathbf{k}}\sum_\lambda \frac{|\Delta_\lambda|^2(\hat n\cdot\hat e_\mu)(\hat n\cdot\hat e_\nu)}{E_\lambda^2(E_\lambda + \text{partner})}}_{\text{intra-helicity pp, subleading}} + O\!\left(\frac{\Delta^2}{b_{\min}^2}\right).$$

The intra-helicity pp piece, evaluated at $T=0$, scales as

$$\int d\xi\,\frac{|\Delta_\lambda|^2}{E_\lambda^2 \cdot 2E_\lambda} \sim \frac{|\Delta_\lambda|^2}{|\Delta_\lambda|} \cdot \frac{1}{|\Delta_\lambda|} = O(1)$$

per helicity sheet — wait, this is not small. Let me redo this.

### Correction: The Real Error Structure

The statement $O(\Delta^2/b_{\min}^2)$ requires a more careful argument. Let me redo it properly.

The key observation is that the intra-helicity pp piece, weighted by $2(\hat n\cdot\hat e_\mu)^2$, is *not* intrinsically small — it gives the usual BCS longitudinal susceptibility contribution $\chi_N(\hat n\cdot\hat e_\mu)^2[1 - Y_\lambda(T)]$ per helicity sheet. At $T=0$, $Y_\lambda = 0$ and the intra-helicity sector contributes $\chi_N\sum_\lambda w_\lambda\langle \hat n_\mu\hat n_\nu\rangle_\lambda = \chi_N\Pi_{\mu\nu}$, which *cancels* against the inter-helicity $-\chi_N\Pi_{\mu\nu}$ — this is precisely the "phase-space cancellation identical to the normal-state computation" the paper refers to. Let me re-verify.

Actually, reading Sec. IV.A carefully: at $T_c$, the ph sector gives $\chi_N \delta_{\mu\nu}$ as the sum of $\chi_N \Pi_{\mu\nu}$ (intra) and $\chi_N(\delta_{\mu\nu} - \Pi_{\mu\nu})$ (inter). At $T=0$ in strong locking, the pp sector gives **only** $\chi_N(\delta_{\mu\nu} - \Pi_{\mu\nu})$ because the intra-helicity pp contribution is killed — not by smallness of $\Delta/b$, but by the fact that the Cooper pair of intra-helicity electrons on a single spin-polarized sheet exists and gaps out the longitudinal response. So the "intra-pp is negligible" phrasing is **wrong**; the correct statement is:

**The intra-helicity pp *does* contribute to $\chi^{pp}_{\mu\nu}(0)$, proportional to $\Pi_{\mu\nu}$, but the longitudinal response of a gapped sheet is already zero at $T=0$ by the Yosida argument** — i.e., the intra-helicity sector's $T=0$ longitudinal $\chi$ is zero, so the intra-pp piece and the intra-ph piece that *would* combine to $\chi_N\Pi_{\mu\nu}$ at $T_c$ cancel to zero at $T=0$.

So the correct accounting at $T=0$ is:

- Intra-helicity contribution: $\chi_N\Pi_{\mu\nu}[1 - Y_\lambda(0)] = 0$ (fully gapped, $Y_\lambda(0)=0$).
- Inter-helicity contribution: $\chi_N(\delta_{\mu\nu} - \Pi_{\mu\nu})$, identical to normal-state computation up to $O(\Delta/b)$ corrections in the denominator.

**The error $O(\Delta^2/b_{\min}^2)$ is then the correction to the inter-helicity denominator**: replacing $E_+ + E_- \to 2b_{\mathbf{k}} + O(\Delta^2/b_{\mathbf{k}})$ introduces a fractional correction $O(\Delta^2/b_{\mathbf{k}}^2)$ to $\chi^{\rm inter}$.

### Recommendation to the Paper

The current one-line argument in Sec. IX.B is **misleading about the source of the error**. I recommend rewriting as follows.

### Suggested Rewrite of Sec. IX.B

Replace the paragraph between "When the minimum locking magnitude…" and Eq. (29) with:

```latex
When the minimum locking magnitude over the FS satisfies
\begin{equation}
	b_{\min}(\mathbf{H})\equiv\min_{\mathbf{k}\in\rm FS}|\mathbf{b}_{\mathbf{k}}|\;\gg\;\Delta,
	\label{eq:strong-locking-H}
\end{equation}
the BdG problem admits a controlled expansion in $\Delta/b$. We sketch the error estimate because it controls the validity range of every finite-field statement below.

Rotate at each $\mathbf{k}$ to the helicity basis of $H_{0}(\mathbf{k})$, with spin quantization axis $\hat n_{\mathbf{k}}(\mathbf{H})$. To zeroth order in $\Delta/b_{\mathbf{k}}$, BdG decouples into two intra-helicity $2\times 2$ blocks with gaps $|\Delta_{\lambda}(\mathbf{k})|$ and standard BCS coherence factors $u_{\lambda},v_{\lambda}$. The $T=0$ spin susceptibility decomposes accordingly into intra-helicity and inter-helicity contributions.

The intra-helicity contribution is $\chi_{N}\Pi_{\mu\nu}(\mathbf{H})[1-Y_{\lambda}(0)]=0$ for a fully gapped state: it vanishes identically as the longitudinal response of a fully polarized, fully gapped sheet, exactly as in the standard Yosida argument. This is \emph{not} a smallness-in-$\Delta/b$ statement; it is the usual $T=0$ gapping of longitudinal spin response on a single helicity sheet.

The inter-helicity contribution reproduces the normal-state matrix-element structure of Eq.~\eqref{eq:me-inter} with the zero-field locking vector replaced by $\hat n_{\mathbf{k}}(\mathbf{H})$. Its denominator is $E_{+}+E_{-}=2b_{\mathbf{k}}+O(\Delta^{2}/b_{\mathbf{k}})$, where the subleading piece arises from expanding $E_{\lambda}=\sqrt{\xi_{\lambda}^{2}+|\Delta_{\lambda}|^{2}}$ around $|\xi_{\lambda}|=b_{\mathbf{k}}$. Phase-space cancellation identical to the normal-state calculation of Sec.~\ref{sec:anisoT0} then yields
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0,\mathbf{H})=\chi_N\big[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})\big]+O\!\big(\Delta^2/b_{\min}^2\big),\;}
	\label{eq:strongH-identity}
\end{equation}
with the field-dependent projection tensor
\begin{equation}
	\Pi_{\mu\nu}(\mathbf{H})\equiv\big\langle\hat n_{\mu}(\mathbf{k};\mathbf{H})\,\hat n_{\nu}(\mathbf{k};\mathbf{H})\big\rangle_{\rm FS}.
	\label{eq:Pi-H}
\end{equation}
The residual $O(\Delta^{2}/b_{\min}^{2})$ combines three sources of the same parametric size: (i) the denominator correction above; (ii) mixing of intra- and inter-helicity sectors by off-diagonal gap components $\Delta_{\perp}$ at $O(\Delta/b)$, whose contribution to $\chi$ is $O(\Delta^{2}/b^{2})$; and (iii) deviations of the coherence factors from the strong-locking limit, again at $O(\Delta^{2}/b^{2})$. For typical NMR-field Rashba superconductors with $gk_{F}\sim 10\,\Delta$, the correction is $\lesssim 1\%$ and well below Knight-shift experimental resolution.
```

### Additional Recommendation: Name the Error in a Worked Case

Sec. IX.D is the natural place to quote a concrete number. Add one sentence to the "Regime diagram and limitations" subsection:

```latex
For illustration, at $gk_{F}=10\Delta$ and $\mu_{B}H=0.1\,gk_{F}$, $b_{\min}/\Delta\approx 9$ and the leading correction to Eq.~\eqref{eq:strongH-identity} is $\sim(\Delta/b_{\min})^{2}\approx 1\%$, comfortably below current Knight-shift resolution.
```

### What Changed

1. **Removed** the incorrect phrasing "intra-band pp contribution is $O(\Delta^2/b^2)$ and negligible." It is not small in $\Delta/b$ — it is zero by the Yosida argument at $T=0$.
2. **Separated three distinct error sources** (denominator, $\Delta_\perp$-mediated mixing, coherence-factor corrections) all of which happen to be the same parametric size $O(\Delta^2/b^2)$, so the $O(\Delta^2/b_{\min}^2)$ claim survives but is now properly sourced.
3. **Connected to the standard Yosida picture** — the longitudinal gapping of a single helicity sheet at $T=0$ is a familiar fact, and using it clarifies why the intra-helicity sector drops out exactly rather than approximately.
4. **Added a concrete numerical size** for typical Rashba scales.

### One Consistency Check for Sec. IV.B

The same logical issue may be present in Sec. IV.B (zero-field strong locking). Re-reading the current Sec. IV.B:

> "When $\mathbf{H}=0$ and $|\mathbf{g}_{\mathbf{k}}|\gg|\mathbf{d}(\mathbf{k})|,|\Delta|$ on the FS, the SOC splitting dominates; the intra-band pp term is negligible and the inter-band pp term gives twice Eq. (17b)…"

Same issue: "intra-band pp term is negligible" is misleading. It's zero at $T=0$ by Yosida, not small in $\Delta/g$. I recommend a parallel minimal edit:

**Replace**: "the intra-band pp term is negligible"

**With**: "the intra-band pp contribution vanishes at $T=0$ by the Yosida argument (fully gapped longitudinal response on each helicity sheet)"

This aligns Secs. IV.B and IX.B on a correct and unified physical picture.

Ready for **issue #7 (Fig. 1 caption)** when you are, or we can jump to a different priority item you'd rather address first.

---
## 🧑‍💻 User

Could you give me the latex code for One Consistency Check for Sec. IV.B?

---
## 🤖 Assistant

## LaTeX for the Sec. IV.B Consistency Fix

Here is the minimal edit. Replace the current opening paragraph of Sec. IV.B (the paragraph immediately before Eq. 19, the boxed strong-locking identity) with:

```latex
\subsection{Strong-locking identity at $T=0$}

When $\mathbf{H}=0$ and $|\mathbf{g}_{\mathbf{k}}|\gg|\mathbf{d}(\mathbf{k})|,|\Delta|$ on the FS, the SOC splitting dominates and a controlled expansion in $\Delta/|\mathbf{g}_{\mathbf{k}}|$ is available. To zeroth order, BdG decouples into two intra-helicity $2\times 2$ blocks with standard BCS coherence factors. The intra-helicity pp contribution vanishes at $T=0$ by the Yosida argument: it is the longitudinal response of a fully polarized, fully gapped helicity sheet, identically zero rather than parametrically small. The surviving inter-helicity pp term reproduces the normal-state matrix-element structure of Eq.~\eqref{eq:me-inter} with denominator $2|\mathbf{g}_{\mathbf{k}}|+O(\Delta^{2}/|\mathbf{g}_{\mathbf{k}}|)$. Phase-space cancellation identical to the normal-state computation then yields
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}],\qquad\mathbf{H}=0,\;|\mathbf{g}_{\mathbf{k}}|/\Delta\to\infty,\;}
	\label{eq:strongSOCid}
\end{equation}
with corrections of order $\Delta^{2}/g_{\min}^{2}$ from the same three sources catalogued below Eq.~\eqref{eq:strongH-identity}. Consequences: trace universality $\mathrm{Tr}\,\chi(0)=2\chi_{N}$ for any FS/SOC; non-zero off-diagonal $\chi_{\mu\nu}(0)$ for tilted SOC; eigenvectors of $\Pi$ define spin-lock principal axes with $\pi_{1}+\pi_{2}+\pi_{3}=1$.
```

### What Changed

1. **"the intra-band pp term is negligible"** → "vanishes at $T=0$ by the Yosida argument" with the physical reason given in one clause.
2. **Added "identically zero rather than parametrically small"** to forestall the misreading that this is an order-of-magnitude estimate.
3. **Added explicit $\Delta^2/g_{\min}^2$ error term** in the boxed equation, paralleling Eq. (29) in Sec. IX. Previously Sec. IV.B's boxed identity carried no error estimate while Sec. IX.B's did — now they are consistent.
4. **Forward-reference to "the three sources catalogued below Eq. (29)"** avoids duplicating the error-source breakdown. The reader can choose to look ahead or accept it on credit.

### Optional Tightening

If you want Sec. IV.B to stand on its own without forward reference, replace the phrase "from the same three sources catalogued below Eq. (29)" with:

```latex
from (i) the inter-helicity denominator expansion above, (ii) $\Delta_{\perp}$-mediated intra-/inter-helicity mixing at $O(\Delta/g)$ contributing $O(\Delta^{2}/g^{2})$ to $\chi$, and (iii) coherence-factor corrections of the same parametric size.
```

This makes the section self-contained at the cost of one extra sentence. Your call which version reads better given how readers will likely encounter the paper.

Ready for **issue #7 (Fig. 1 caption length)** when you are.

---
## 🧑‍💻 User

go with issue #7

---
## 🤖 Assistant

## Issue #7: Fig. 1 (Simplex) Caption Length

### The Problem

The current caption runs to ~200 words and contains four distinct kinds of content:

1. Definition of the simplex (what it represents).
2. Classification of the three vertex types (oblate axial).
3. Classification of the three edge-midpoint types (prolate axial).
4. The barycenter (isotropic).
5. Interior points (tilted textures).
6. The intermediate-SOC contraction arrow and its formula.

Figure captions are for **reading the figure**, not for teaching the content. Items 2–5 are covered by Table III (pairing-class catalogue) in the same subsection. Item 6 is explained in prose in Sec. VII.C. The caption currently duplicates both.

### Recommended Rewrite

Strip the caption to the minimum needed to read the figure, and move the classification content into the main text (where it is already partially covered anyway).

**Minimal caption:**

```latex
\caption{Simplex of allowed $T=0$ Knight-shift ellipsoids in the strong-locking regime, parametrized by the eigenvalues $(\pi_{1},\pi_{2},\pi_{3})$ of $\Pi$ with $\sum_{i}\pi_{i}=1$, $\pi_{i}\in[0,1]$ [Eq.~\eqref{eq:Kellipsoid}]. Vertices (black): oblate-axial ellipsoids from OSP triplet or quasi-1D SOC along one crystal axis. Edge midpoints (red): prolate-axial ellipsoids from ESP triplet in a plane or 2D Rashba SOC confined to that plane. Barycenter (blue): isotropic sphere from singlet with strong SOC or isotropic 3D SOC. Interior points correspond to tilted locking textures. Blue arrow: radial contraction of a strong-locking point toward the origin at intermediate SOC (for uniform $|\mathbf{g}|/\Delta$, $p_{i}=F_{s}(\lambda)\pi_{i}$; see Sec.~\ref{sec:ellipsoid}). Full classification in Table~\ref{tab:ellipsoids}.}
```

This is ~95 words — cut by more than half — and every sentence serves the figure rather than the narrative.

### What the Main Text Needs

The rewritten caption drops the detailed descriptions of each vertex/edge ("the response vanishes along that axis and is $K_N$ in the transverse plane", etc.). Those details are already in Table III, so no new main-text content is needed. However, to preserve the reader's ability to scan the figure and understand the shapes immediately, one short paragraph in Sec. X.C should point at Table III explicitly. Look for the sentence:

> "Four observations make the table an experimental diagnostic."

Preceding it, consider adding:

```latex
Figure~\ref{fig:simplex} and Table~\ref{tab:ellipsoids} together form the classification: the simplex identifies where a measured point sits, and the table gives the corresponding pairing/texture interpretation and principal-value ratios.
```

This makes explicit that Fig. 1 and Table III are a matched pair — the figure is the map, the table is the legend.

### Optional: Tighten the TikZ Node Labels Too

The current TikZ has multi-line labels like:

```latex
\node[below=3pt, align=center, font=\scriptsize] at (V1) {$(1,0,0)$\\ OSP $\mathbf{d}\|\hat a$\\ or quasi-1D $\|\hat a$};
```

These repeat the classification in the caption. If you accept the caption rewrite, consider shortening the TikZ labels to just the coordinates:

```latex
\node[below=3pt, font=\scriptsize] at (V1) {$(1,0,0)$};
\node[below=3pt, font=\scriptsize] at (V2) {$(0,1,0)$};
\node[above=3pt, font=\scriptsize] at (V3) {$(0,0,1)$};
\node[below=4pt, font=\scriptsize] at (M12) {$(\tfrac{1}{2},\tfrac{1}{2},0)$};
\node[left=4pt, font=\scriptsize] at (M13) {$(\tfrac{1}{2},0,\tfrac{1}{2})$};
\node[right=4pt, font=\scriptsize] at (M23) {$(0,\tfrac{1}{2},\tfrac{1}{2})$};
\node[right=6pt, font=\scriptsize] at (B) {$(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$};
```

The physical interpretation is then one table lookup away, and the figure becomes much cleaner. The arrow label can also be shortened to just "intermediate SOC" since the formula is in the caption.

This is a judgment call — some readers prefer the figure to be self-contained, others prefer a clean geometric object. Given that Table III is immediately adjacent to the figure in the manuscript, I lean toward the clean version, but the choice is yours.

Ready for **issue #8 (Table II saturation pattern — adding a physical interpretation column)**?

---
## 🧑‍💻 User

Could you give me the updated figure paragraph?

---
## 🤖 Assistant

## Updated Fig. 1 Block (TikZ + Caption)

Here is the complete replacement for the `figure` environment in Sec. X.C, combining the tightened caption, the simplified TikZ labels, and consistent styling.

```latex
\begin{figure}[tb]
	\centering
	\begin{tikzpicture}[scale=3.2, font=\small]
		\coordinate (V1) at (-1, 0);
		\coordinate (V2) at ( 1, 0);
		\coordinate (V3) at ( 0, 1.7320508);
		\coordinate (M12) at ( 0, 0);
		\coordinate (M13) at (-0.5, 0.8660254);
		\coordinate (M23) at ( 0.5, 0.8660254);
		\coordinate (B) at ( 0, 0.5773503);
		\fill[gray!8] (V1) -- (V2) -- (V3) -- cycle;
		\draw[thick] (V1) -- (V2) -- (V3) -- cycle;
		\draw[gray!55, dashed, thin] (V1) -- (M23);
		\draw[gray!55, dashed, thin] (V2) -- (M13);
		\draw[gray!55, dashed, thin] (V3) -- (M12);
		\fill (V1) circle (0.024);
		\fill (V2) circle (0.024);
		\fill (V3) circle (0.024);
		\fill[red!80!black] (M12) circle (0.024);
		\fill[red!80!black] (M13) circle (0.024);
		\fill[red!80!black] (M23) circle (0.024);
		\fill[blue!70!black] (B) circle (0.033);
		\node[below=3pt, font=\scriptsize] at (V1) {$(1,0,0)$};
		\node[below=3pt, font=\scriptsize] at (V2) {$(0,1,0)$};
		\node[above=3pt, font=\scriptsize] at (V3) {$(0,0,1)$};
		\node[below=4pt, font=\scriptsize] at (M12) {$(\tfrac{1}{2},\tfrac{1}{2},0)$};
		\node[left=4pt, font=\scriptsize] at (M13) {$(\tfrac{1}{2},0,\tfrac{1}{2})$};
		\node[right=4pt, font=\scriptsize] at (M23) {$(0,\tfrac{1}{2},\tfrac{1}{2})$};
		\node[right=6pt, font=\scriptsize] at (B) {$(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$};
		\draw[->, thick, blue!60!black, shorten >=1pt] ($(B)+(210:0.28)$) -- ($(B)+(210:0.02)$);
		\node[below left=1pt, font=\scriptsize, blue!60!black] at ($(B)+(210:0.28)$) {intermediate SOC};
	\end{tikzpicture}
	\caption{Simplex of allowed $T=0$ Knight-shift ellipsoids in the strong-locking regime, parametrized by the eigenvalues $(\pi_{1},\pi_{2},\pi_{3})$ of $\Pi$ with $\sum_{i}\pi_{i}=1$, $\pi_{i}\in[0,1]$ [Eq.~\eqref{eq:Kellipsoid}]. Vertices (black): oblate-axial ellipsoids from OSP triplet or quasi-1D SOC along one crystal axis. Edge midpoints (red): prolate-axial ellipsoids from ESP triplet in a plane or 2D Rashba SOC confined to that plane. Barycenter (blue): isotropic sphere from singlet with strong SOC or isotropic 3D SOC. Interior points correspond to tilted locking textures. Blue arrow: radial contraction of a strong-locking point toward the origin at intermediate SOC (for uniform $|\mathbf{g}|/\Delta$, $p_{i}=F_{s}(\lambda)\pi_{i}$; see Sec.~\ref{sec:ellipsoid}). Full classification in Table~\ref{tab:ellipsoids}.}
	\label{fig:simplex}
\end{figure}
```

### Summary of Changes

1. **Vertex/edge/barycenter labels** reduced to bare coordinates. Physical interpretation is now one lookup away in Table III, which sits immediately after this figure in the manuscript.
2. **Arrow label** shortened from "intermediate SOC: $\langle F_s\rangle\!\uparrow$" to just "intermediate SOC"; the quantitative formula lives in the caption.
3. **Caption** rewritten from ~200 words to ~95 words. Structure: (i) what the figure represents, (ii) what the three highlighted point types mean geometrically, (iii) what the arrow means, (iv) pointer to the classification table.

### One Minor Paragraph Addition in Main Text

To keep the figure–table pairing explicit, add one short sentence to Sec. X.C immediately before "Four observations make the table an experimental diagnostic.":

```latex
Figure~\ref{fig:simplex} and Table~\ref{tab:ellipsoids} together form the classification: the simplex identifies where a measured point sits, and the table gives the corresponding pairing/texture interpretation and principal-value ratios.
```

Ready for **issue #8 (Table II saturation — physical interpretation column)** when you are.

---
## 🧑‍💻 User

go with issue # 8

---
## 🤖 Assistant

## Issue #8: Table II (Saturation Pattern) Needs a Physical Interpretation

### The Problem

Current Table II lists five limiting cases with their $T=0$ susceptibility components and the trace ratio $\mathrm{Tr}\chi/\chi_N$:

| Pairing / limit | $\chi_{xx}(0)$ | $\chi_{yy}(0)$ | $\chi_{zz}(0)$ | Tr$/\chi_N$ |

The reader can see that most cases saturate the $2\chi_N$ bound, but the table does not explain *why* or what "saturation" means physically. Three readings are possible, and the paper does not distinguish them:

1. **Saturation of the scalar trace bound** $\mathrm{Tr}\chi(0) \le 2\chi_N$ — the statement of Sec. IV.
2. **Full trace $\mathrm{Tr}\Pi = 1$** on the locking projector — a geometric fact about whatever locking vector is active.
3. **Absence of a Yosida-type gapping in the transverse channel** — the physical reason $\chi_{\mu\mu}$ retains part of its normal-state value.

These are consistent but not identical, and a reader glancing at the table wants to know which strict inequalities hold and which are saturated identities.

### Recommended Restructuring

Add a **locking vector** column and a **saturation mechanism** column. Replace the explanatory paragraph underneath with a two-sentence summary.

### Suggested Rewrite

```latex
\begin{table}[tb]
	\caption{Saturation of the trace bound $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ in canonical limits. Components in units of $\chi_{N}$. The "locking vector" column gives the unit vector $\hat n_{\mathbf{k}}$ entering Eq.~\eqref{eq:unified}; "mechanism" indicates whether the locking exists because of SOC ($\hat g$), the triplet $\mathbf{d}$-vector ($\hat d$), or is absent (---). The bound is saturated whenever a well-defined locking direction exists on the FS.}
	\label{tab:sat}
	\renewcommand\arraystretch{1.3}
	\setlength{\tabcolsep}{0.4ex}
	\begin{tabular}{l|ccc|c|ll}
		\hline\hline
		Pairing / limit & $\chi_{xx}(0)$ & $\chi_{yy}(0)$ & $\chi_{zz}(0)$ & Tr$/\chi_{N}$ & Locking $\hat n_{\mathbf{k}}$ & Mechanism \\
		\hline
		$s$-wave, $g=\mathbf{H}=0$ & $0$ & $0$ & $0$ & $0$ & --- & no locking (Yosida)\\
		$s$-wave, $gk_{F}\!\gg\!\Delta$ & $2/3$ & $2/3$ & $2/3$ & $2$ & $\hat g_{\mathbf{k}}$ & SOC ($\langle\hat g_{\mu}^{2}\rangle=1/3$)\\
		OSP ($\mathbf{d}\!\parallel\!\hat z$), $g=\mathbf{H}=0$ & $1$ & $1$ & $0$ & $2$ & $\hat z$ & $\mathbf{d}$-vector\\
		ESP ($\mathbf{d}\!\in\!xy$), $g=\mathbf{H}=0$ & $1/2$ & $1/2$ & $1$ & $2$ & $\hat d_{\mathbf{k}}\in xy$ & $\mathbf{d}$-vector\\
		any unitary $p$-wave, $gk_{F}\!\gg\!\Delta$ & $2/3$ & $2/3$ & $2/3$ & $2$ & $\hat g_{\mathbf{k}}$ & SOC dominates\\
		\hline\hline
	\end{tabular}
\end{table}
```

And replace the text below the table ("Every unitary triplet saturates the bound already at $g=\mathbf{H}=0$. Strong Rashba SOC drives every pairing to $\chi_{\mu\mu}(0)\to(2/3)\chi_N$. The only strict case is spin-singlet with weak SOC, made explicit in Sec. VII.") with:

```latex
The table illustrates the general content of Eq.~\eqref{eq:unified}: the trace bound is saturated as an identity ($\mathrm{Tr}\,\chi(0)=2\chi_{N}$) whenever the locking vector $\hat n_{\mathbf{k}}$ is well defined on the FS, because $\mathrm{Tr}\,\Pi=1$. The only strict inequality arises in the spin-singlet, weak-SOC regime, where no locking is enforced and the transverse response is gapped by the standard Yosida mechanism; this is the case made quantitative by $F_{s}(\lambda)$ in Sec.~\ref{sec:intermediate}.
```

### What Changed

1. **Added a "Locking $\hat n_{\mathbf{k}}$" column.** The reader now sees the geometric object entering Eq. (22) explicitly — SOC direction, $\mathbf{d}$-vector, or absent — for each row.

2. **Added a "Mechanism" column.** Distinguishes the three different physical origins of locking that all produce the same $\mathrm{Tr}\chi(0)=2\chi_N$ via the same $\mathrm{Tr}\Pi=1$ identity:
   - SOC-driven locking ($\hat g_{\mathbf{k}}$)
   - Triplet-driven locking ($\hat d_{\mathbf{k}}$)
   - No locking (Yosida regime)

3. **Explanatory text tightened and refocused.** Previously, the text stated three facts separately ("every unitary triplet saturates", "strong Rashba drives every pairing to $2/3$", "singlet+weak SOC is strict"). These are all consequences of one fact: saturation is equivalent to existence of a well-defined locking vector. The new text says this directly and points forward to Sec. VII for the only non-saturated case.

4. **The $\langle\hat g_\mu^2\rangle = 1/3$ parenthetical** in row 2 makes explicit where the $2/3$ in the $s$-wave strong-SOC case comes from — it's the specific numerical consequence of FS isotropy for the $s$-wave row, not a universal feature of saturation.

### Optional Further Tightening

If the extra two columns make the table feel crowded, you can drop the "Mechanism" column and merge the information into the "Locking $\hat n_{\mathbf{k}}$" column header, e.g., "$\hat z$ (from $\mathbf{d}$)" instead of a separate column. The seven-column version above is cleaner but wider; the six-column version is more compact. Your call depending on how the table renders in the PRB two-column layout.

Ready for **issue #9 (notational consistency across the paper)** when you are.

---
## 🧑‍💻 User

go with issue #9

---
## 🤖 Assistant

## Issue #9: Notational Consistency Across the Paper

A full audit turned up six places where notation drifts or is introduced more than once. Rather than list them abstractly, here is what to do concretely.

### A. Add a Notation Table to Sec. II

The cleanest fix for the general reader is a small glossary inserted after Eq. (5) (the $\Pi_{\mu\nu}$ definition). This also serves as a reference card for the manual sections.

```latex
\begin{table}[tb]
	\caption{Key symbols used throughout.}
	\label{tab:notation}
	\renewcommand\arraystretch{1.2}
	\setlength{\tabcolsep}{0.6ex}
	\begin{tabular}{l|l}
		\hline\hline
		Symbol & Meaning \\
		\hline
		$\mathbf{g}_{\mathbf{k}}$ & antisymmetric SOC vector, $\mathbf{g}_{-\mathbf{k}}=-\mathbf{g}_{\mathbf{k}}$ \\
		$\mathbf{b}_{\mathbf{k}}$ & combined locking field $\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}$ \\
		$\hat n_{\mathbf{k}}$ & unit locking vector $\mathbf{b}_{\mathbf{k}}/|\mathbf{b}_{\mathbf{k}}|$ (Eq.~\eqref{eq:ndef}) \\
		$\psi(\mathbf{k}),\mathbf{d}(\mathbf{k})$ & singlet and triplet pairing amplitudes (Eq.~\eqref{eq:Delta-gen}) \\
		$\lambda_{\mathbf{k}}$ & dimensionless SOC $|\mathbf{g}_{\mathbf{k}}|/\Delta$ \\
		$h$ & dimensionless Zeeman $\mu_{B}|\mathbf{H}|/\Delta$ \\
		$\Pi_{\mu\nu}$ & FS projector $\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ (Eq.~\eqref{eq:Pidef}) \\
		$\pi_{i}$ & eigenvalues of $\Pi$, $i=1,2,3$, $\sum_{i}\pi_{i}=1$ \\
		$\chi_{N}$ & Pauli value $2\mu_{B}^{2}N(0)$ \\
		$K_{N}$ & normal-state Knight shift $K(T_{c}^{+})$; scalar hyperfine: $K_{N}=A\chi_{N}$ \\
		$F_{s}(\lambda)$ & $s$-wave SOC interpolation (Eq.~\eqref{eq:Fs}) \\
		$Y_{\lambda}(T)$ & helicity-$\lambda$ Yosida function \\
		$\mathrm{Tr}_{s},\mathrm{Tr}_{\rm BdG}$ & trace over single-particle spin space, over Nambu \\
		$\langle\cdot\rangle_{\rm FS}$ & FS average with DOS weight $N(0)^{-1}$ \\
		$\langle\cdot\rangle_{\lambda}$ & FS average restricted to $\lambda$-helicity sheet \\
		\hline\hline
	\end{tabular}
\end{table}
```

### B. Six Specific Drift Points to Fix

**(1) $\hat n_{\mathbf{k}}$ overloading.**
Sec. II Eq. (3) defines $\hat n_{\mathbf{k}}$ from the combined locking field $\mathbf{b}_{\mathbf{k}}$. Sec. IV.D then re-announces $\hat n$ as "the dominant locking vector ($\hat g_{\mathbf{k}}$, $\hat d_{\mathbf{k}}$, or normalized $\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}$)." The two definitions are compatible in the respective limits but the prose around Eq. (22) reads as if $\hat n$ is being redefined.

**Fix:** rewrite the prose following Eq. (22) to say "with $\hat n_{\mathbf{k}}$ identified with $\hat g_{\mathbf{k}}$ when $\mathbf{H}=0$ and SOC dominates, with $\hat d_{\mathbf{k}}$ in the zero-SOC unitary-triplet limit, and with $\mathbf{b}_{\mathbf{k}}/|\mathbf{b}_{\mathbf{k}}|$ when both fields are present." The word "identified with" makes clear these are limits of one definition, not a new definition each time.

**(2) Introduce $\mathbf{b}_{\mathbf{k}}$ in Sec. II, not Sec. IX.**
Currently $\mathbf{b}_{\mathbf{k}}$ is named only in Eq. (28). Use it already in Eq. (3):

```latex
The normal-state eigenstates of Eq.~\eqref{eq:H0gen} have spins along the unit vector
\begin{equation}
	\hat n_{\mathbf{k}}=\mathbf{b}_{\mathbf{k}}/|\mathbf{b}_{\mathbf{k}}|,\qquad
	\mathbf{b}_{\mathbf{k}}\equiv\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}},
	\label{eq:ndef}
\end{equation}
reducing to $\hat n_{\mathbf{k}}=\hat g_{\mathbf{k}}$ at zero Zeeman field.
```

Sec. IX then uses the same $\mathbf{b}_{\mathbf{k}}$ without reintroduction.

**(3) $K_N$ vs $\chi_N$.**
$K_N$ first appears in Eq. (63) — Sec. X.B — as $K(\hat{\mathbf{H}}, T_c^+)$. For scalar hyperfine $K_N = A\chi_N$; for anisotropic hyperfine the relation is component-by-component, $K_i(T_c^+) = A_i\chi_N$. Sec. X.D mixes both without stating which.

**Fix:** add a one-line explicit connection to Sec. X.A where $K_{\mu\nu}$ is first defined:

```latex
For isotropic hyperfine $A^{(\mathbf{R})}_{\mu\nu}=A\delta_{\mu\nu}$, define $K_{N}\equiv A\chi_{N}$; for diagonal anisotropic hyperfine $A^{(\mathbf{R})}=\mathrm{diag}(A_{1},A_{2},A_{3})$, we reserve $K_{N}$ for the scalar-hyperfine case and write $K_{i}(T_{c}^{+})=A_{i}\chi_{N}$ component-by-component.
```

Then Sec. X.D uses $K_i(T_c^+)$ consistently and avoids ambiguity.

**(4) $\pi_\mu$ vs $\pi_i$ vs $\Pi_{\mu\mu}$.**
Three related but distinct objects are in use:
- $\Pi_{\mu\nu}$ — full tensor in Cartesian components.
- $\Pi_{\mu\mu}$ (no sum) — diagonal components in Cartesian frame; appears in Sec. IV.A and Sec. VIII.
- $\pi_i$, $i=1,2,3$ — eigenvalues of $\Pi$; appears in Sec. X.
- $\pi_\mu$ — used in Sec. VIII (e.g., "$\chi_N\pi_\mu$"), implicitly $\Pi_{\mu\mu}$ in the principal-axis frame.

**Fix:** standardize.
- Use $\Pi_{\mu\mu}$ (diagonal Cartesian component, no sum) wherever the component refers to a fixed lab axis $\mu$.
- Use $\pi_i$ (eigenvalue index $i$) wherever principal-axis coordinates are meant.
- Drop $\pi_\mu$ entirely; it is ambiguous.

Concretely, in Sec. VIII replace every $\pi_\mu$ with $\Pi_{\mu\mu}$. The spin-FGT sum rule becomes $\chi_N - \chi_{\mu\mu}(0) = \chi_N\Pi_{\mu\mu}$, which is exact: when $\mu$ happens to be a principal axis, $\Pi_{\mu\mu} = \pi_i$ for some $i$, but the notation no longer presumes that.

**(5) Crystal axis notation: $(x,y,z)$ vs $(a,b,c)$.**
Sec. IV and Table III use $(x,y,z)$. Fig. 1, Sec. X.D, Sec. XI (protocols), and Sec. XII all use $(a,b,c)$.

**Fix:** use $(x,y,z)$ as the generic Cartesian labels throughout the theory sections (Secs. II–X) and $(a,b,c)$ only in material-specific contexts (Sec. XII and the K$_2$Cr$_3$As$_3$ parts of the protocols). Add one sentence at the start of Sec. X.D: "For the K$_2$Cr$_3$As$_3$ application of Sec.~\ref{sec:K2Cr3As3}, $(x,y,z)$ is identified with the hexagonal $(a,b,c)$ frame." This separates the generic from the specific without a global rename.

**(6) $\Delta$ vs $\psi$ for the singlet amplitude.**
Issue #4 already set up Sec. II with $\psi(\mathbf{k})$ as the singlet amplitude, consistent with Sec. V Eq. (23). But Sec. VII ("intermediate SOC, $s$-wave") uses $\Delta$ as the singlet amplitude throughout Eqs. (19)–(22), and Sec. IX similarly writes the strong-locking regime with a scalar "$\Delta$."

**Fix:** add a one-line bridge at the start of Sec. VII:

```latex
In this section we specialize to pure $s$-wave pairing, $\psi(\mathbf{k})=\Delta$ and $\mathbf{d}(\mathbf{k})=0$, and henceforth denote the singlet amplitude simply by $\Delta$.
```

And a parallel bridge at the start of Sec. IX:

```latex
Throughout this section "$\Delta$" denotes a representative pairing scale, equal to $\psi$ in the singlet limit and to $|\mathbf{d}|$ for a fully gapped unitary triplet.
```

### C. Small Typography Fixes

- `Rashiba1960` → `Rashba1960` (citation key typo, already flagged).
- `Frigeri2004` and `Frigeri_2004` appear both; check whether these are intended as two references or a single duplicate. If duplicate, merge in the `.bib` file.
- `Samohkin15` should presumably be `Samokhin15`.

### D. Rollout Order

If applied in this order, no edit breaks any other:

1. Add Table I (notation glossary) to Sec. II.
2. Introduce $\mathbf{b}_{\mathbf{k}}$ in Eq. (3).
3. Rewrite prose after Eq. (22).
4. Add isotropic/anisotropic hyperfine distinction in Sec. X.A.
5. Replace $\pi_\mu \to \Pi_{\mu\mu}$ in Sec. VIII.
6. Add the one-line bridges for $\Delta$ in Secs. VII and IX.
7. Add $(x,y,z)$ vs $(a,b,c)$ note in Sec. X.D.
8. Fix citation-key typos in `.bib`.

This completes the original list of nine improvement areas we discussed. Let me know whether you'd like to:

- Tackle something beyond the original list (e.g., the scope paragraph in the introduction, the reference-table entries I flagged in passing, or a reread of any specific section).
- Go deeper on any of the fixes we've done — e.g., draft the full notation table entries in the style of a glossary.
- Close the review.

---
## 🧑‍💻 User

In the new table, the row of K_N is too wide

---
## 🤖 Assistant

## Fix: Shorten the $K_N$ Row

The long entry is causing the overflow. Two options, both tight:

**Option 1 (minimal):** drop the scalar-hyperfine qualifier and keep only the definition. The $K_N = A\chi_N$ relation is spelled out explicitly in Sec. X.A where it belongs.

```latex
$K_{N}$ & normal-state Knight shift, $K_{N}\equiv K(T_{c}^{+})$ \\
```

**Option 2 (compact with relation kept):** use a shorter phrasing and inline math.

```latex
$K_{N}$ & normal-state Knight shift $K(T_{c}^{+})=A\chi_{N}$ \\
```

I'd recommend Option 1. The table is a glossary, not a derivation sheet; the hyperfine map belongs in Sec. X where anisotropic hyperfine is discussed anyway.

### Full Revised Table

```latex
\begin{table}[tb]
	\caption{Key symbols used throughout.}
	\label{tab:notation}
	\renewcommand\arraystretch{1.2}
	\setlength{\tabcolsep}{0.6ex}
	\begin{tabular}{l|l}
		\hline\hline
		Symbol & Meaning \\
		\hline
		$\mathbf{g}_{\mathbf{k}}$ & antisymmetric SOC vector, $\mathbf{g}_{-\mathbf{k}}=-\mathbf{g}_{\mathbf{k}}$ \\
		$\mathbf{b}_{\mathbf{k}}$ & combined locking field $\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}$ \\
		$\hat n_{\mathbf{k}}$ & unit locking vector $\mathbf{b}_{\mathbf{k}}/|\mathbf{b}_{\mathbf{k}}|$ (Eq.~\eqref{eq:ndef}) \\
		$\psi(\mathbf{k}),\mathbf{d}(\mathbf{k})$ & singlet and triplet pairing amplitudes (Eq.~\eqref{eq:Delta-gen}) \\
		$\lambda_{\mathbf{k}}$ & dimensionless SOC $|\mathbf{g}_{\mathbf{k}}|/\Delta$ \\
		$h$ & dimensionless Zeeman $\mu_{B}|\mathbf{H}|/\Delta$ \\
		$\Pi_{\mu\nu}$ & FS projector $\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ (Eq.~\eqref{eq:Pidef}) \\
		$\pi_{i}$ & eigenvalues of $\Pi$, $i=1,2,3$, $\sum_{i}\pi_{i}=1$ \\
		$\chi_{N}$ & Pauli value $2\mu_{B}^{2}N(0)$ \\
		$K_{N}$ & normal-state Knight shift, $K_{N}\equiv K(T_{c}^{+})$ \\
		$F_{s}(\lambda)$ & $s$-wave SOC interpolation (Eq.~\eqref{eq:Fs}) \\
		$Y_{\lambda}(T)$ & helicity-$\lambda$ Yosida function \\
		$\mathrm{Tr}_{s},\mathrm{Tr}_{\rm BdG}$ & trace over single-particle spin space, over Nambu \\
		$\langle\cdot\rangle_{\rm FS}$ & FS average with DOS weight $N(0)^{-1}$ \\
		$\langle\cdot\rangle_{\lambda}$ & FS average restricted to $\lambda$-helicity sheet \\
		\hline\hline
	\end{tabular}
\end{table}
```

All rows should now fit within the single-column width.

---
## 🧑‍💻 User

This is the revised version.

---
## 🤖 Assistant

## Review of the Revised Version

The revised manuscript incorporates the major structural changes from issues #1–#8. There are a few loose ends, mostly broken cross-references from the restructuring. Let me flag them in order of severity.

### Critical: Broken Label References

These will produce `??` in the rendered PDF and need fixing.

**1. `eq:universal-23` no longer exists.** In Table IV (`tab:keyresults`), entry #2 says:
```latex
... & Eq.~\eqref{eq:universal-23}\
```
The label was replaced by `eq:spin-23` in the revised Sec. III.D. Fix:
```latex
... & Eq.~\eqref{eq:spin-23}\\
```
Also update the statement and domain columns for that row to reflect the qualified spin-only bound:
```latex
2 & Spin $T=0$ bound & $\chi_{\mu\mu}(0)\le\tfrac{2}{3}\chi_{N}$ & 3D isotropic FS, $O=\sigma_{\mu}$ & Eq.~\eqref{eq:spin-23}\\
```

**2. `eq:T1-bound` no longer exists.** The old heuristic $1/T_1$ equation was replaced by `eq:T1-full-bound` and `eq:T1-diagnostic`. Broken references in four places:

- Table `tab:protocols`, Protocol D failure column: `deficit $>$ RHS of Eq.~\eqref{eq:T1-bound}` → `Eq.~\eqref{eq:T1-diagnostic}`
- Protocol D step 1: `fixes the RHS of Eq.~\eqref{eq:T1-bound}` → `Eq.~\eqref{eq:T1-full-bound}`
- Protocol D bullet inside step 3: `This is the most powerful use of Eq.~\eqref{eq:T1-bound}.` → `Eq.~\eqref{eq:T1-diagnostic}`
- Sec. XII.C: `Applying the spin-FGT budget Eq.~\eqref{eq:T1-bound}` → `Eq.~\eqref{eq:T1-full-bound}`
- Sec. XII.C: `therefore exceeds the RHS of Eq.~\eqref{eq:T1-bound}` → `Eq.~\eqref{eq:T1-diagnostic}`

**3. Table IV entry #13** still carries the "heuristic bound" framing and the old label:
```latex
13 & $1/T_{1}$ heuristic bound & $\int_{0}^{T_{c}}\!\frac{dT}{T}[\cdots]\lesssim\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\pi_{\mu}$ & $\mathbf{q}\approx 0$ dominant & Protocol D\\
```
Update to match the revised Sec. VIII:
```latex
13 & $1/T_{1}$ finite-$\mathbf{q}$ diagnostic & $\delta_{\alpha}>\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\pi_{\alpha}\Rightarrow$ finite-$\mathbf{q}$ dominance & conditional on $\mathbf{q}\approx 0$ averaging & Protocol D\\
```

### Remaining Notational Drift (from Issue #9 that wasn't applied)

These are not broken, but the inconsistency remains:

**4. $\pi_\mu$ in Sec. VIII.** The boxed Eq. `eq:spinFGT` and subsequent equations in Sec. VIII still use $\pi_\mu$. Per Issue #9, should be $\Pi_{\mu\mu}$ (no sum). Search-and-replace in Sec. VIII:
- `\chi_{N}\pi_{\mu}` → `\chi_{N}\Pi_{\mu\mu}`
- `\pi_{z}=1` → `\Pi_{zz}=1`

Same fix in Sec. VIII.E corollary (i), and in Fig. `fig:spinFGT-spectral` caption, and in Table IV entry #12.

**5. Sec. VII $\Delta$ bridge sentence not added.** Suggest inserting at start of Sec. VII:
```latex
In this section we specialize to pure $s$-wave pairing, $\psi(\mathbf{k})=\Delta$ and $\mathbf{d}(\mathbf{k})=0$, and denote the singlet amplitude simply by $\Delta$.
```

**6. Sec. X.A anisotropic hyperfine note not added.** The scalar-hyperfine default is stated, but the connection to Sec. X.D is implicit. One-line fix in Sec. X.A after `Eq.~\eqref{eq:Kdef}`:
```latex
For isotropic hyperfine, $K_{N}\equiv A\chi_{N}$; the diagonal anisotropic case is treated in Sec.~\ref{sec:ellipsoid-hf}.
```

**7. $(x,y,z)$ vs $(a,b,c)$ note.** Sec. X and Table III use $(x,y,z)$; Sec. XI and XII use $(a,b,c)$. Add at start of Sec. XI:
```latex
Throughout Secs.~\ref{sec:protocols}--\ref{sec:K2Cr3As3}, $(a,b,c)$ denotes the crystallographic frame identified with the generic $(x,y,z)$ of the theory sections.
```

### Minor

**8. Protocol D step 3, inner bullet** has a lingering logical ordering issue: it says "A deficit larger than the RHS is a direct, unambiguous diagnostic." This is now Eq. `eq:T1-diagnostic` proper. Consider rephrasing to point at the diagnostic directly:
```latex
\item A deficit \emph{larger} than the RHS triggers the finite-$\mathbf{q}$ diagnostic Eq.~\eqref{eq:T1-diagnostic}: the observation cannot be accommodated by any redistribution of $\mathbf{q}=0$ spectral weight.
```

**9. Fig. `fig:spinFGT-spectral` caption** uses `$\chi_N\pi_\mu$`; per fix #4, should be `$\chi_N\Pi_{\mu\mu}$`.

### Summary

If you apply fixes 1–3 (broken references) the PDF will compile cleanly. Fixes 4–9 are the tail end of the notational-consistency pass and are cosmetic — do them if you want the $\pi_\mu/\Pi_{\mu\mu}$ distinction clean throughout, skip them if the current paper is close to submission.

Let me know if you want me to verify anything else in the revised version, or close out the review.

---
## 🧑‍💻 User

I have fixed some, pls give me the whole paragarph in remaining fixes.

---
## 🤖 Assistant

## Remaining Fixes as Full Paragraphs

Here are the paragraphs to paste in, organized by section. Each block is self-contained.

### Fix 1: Sec. XII.C broken reference to `eq:T1-bound`

Replace the paragraph immediately after Eq. `eq:T1-K2Cr3As3`:

```latex
The first line states that \emph{no} $\mathbf{q}=0$ spectral weight is available to suppress $1/T_{1}\parallel\hat c$. The observed drop in that orientation therefore triggers the diagnostic Eq.~\eqref{eq:T1-diagnostic} and, by Protocol~D, is an unambiguous fingerprint of finite-$\mathbf{q}$ dominance. The natural candidate is the FM spin fluctuations identified in Ref.~\cite{Triplet2021} through the Curie-Weiss enhancement of $1/T_{1}T$ at $T>T_{c}$: they gap out below $T_{c}$ but are not constrained by the $\mathbf{q}=0$ budget. The absence of a Hebel--Slichter peak is a separate signature of the nodal $p$-wave gap structure, consistent with the $E'$ interpretation.
```

### Fix 4: Sec. VIII $\pi_\mu \to \Pi_{\mu\mu}$ throughout

**Sec. VIII.A — Spectral sum rule paragraph containing Eq. `eq:spinFGT`:**

```latex
The uniform spin susceptibility satisfies Kramers--Kronig at $\omega=0$ in both the normal and superconducting states:
\begin{equation}
	\chi_{\mu\mu}(T)=\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\mathrm{Im}\,\chi_{\mu\mu}(\omega,T),
	\label{eq:KK}
\end{equation}
with $\mathrm{Im}\,\chi_{\mu\mu}(\omega)$ odd in $\omega$. Subtracting the two,
\begin{widetext}
\begin{equation}
	\boxed{\;\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\big[\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)-\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega)\big]=\chi_{N}-\chi_{\mu\mu}(0)=\chi_{N}\Pi_{\mu\mu},\;}
	\label{eq:spinFGT}
\end{equation}
\end{widetext}
where $\chi_{\mu\mu}(0)=\chi_{N}(1-\Pi_{\mu\mu})$ is the strong-locking identity Eq.~\eqref{eq:unified}. Equation~\eqref{eq:spinFGT} is the spin analogue of the Ferrell--Glover--Tinkham optical sum rule: \emph{the weighted spectral weight removed from the superconducting state at each frequency equals the Knight-shift deficit}, itself a geometric quantity determined by the FS average $\Pi_{\mu\mu}=\langle(\hat n\cdot\hat e_{\mu})^{2}\rangle_{\rm FS}$.
```

**Sec. VIII.B — closing sentence:**

```latex
In the normal state at $T_{c}^{+}$, only the ph channel contributes, with spectral support at the interband splitting $2|\mathbf{b}_{\mathbf{k}}|$ (Van Vleck) and a Landau damping contribution at $\omega\to 0$ (Pauli). Equation~\eqref{eq:general-sum-rule} fixes the \emph{total} squared matrix-element weight,
\begin{equation}
	\sum_{s_{1}s_{2}}\big[|M_{ph,\mu}|^{2}+|M_{pp,\mu}|^{2}\big]=2,
	\label{eq:total-weight}
\end{equation}
per $\mathbf{k}$, so the \emph{total} oscillator strength, suitably weighted, is conserved across the superconducting transition. Spectral weight originally in the Pauli term at $\omega=0$ in the normal state is partially transferred into a continuum above $\omega=2\Delta_{\min}$ in the SC state, with the missing static response set by $\Pi_{\mu\mu}$.
```

**Sec. VIII.C — both paragraphs:**

```latex
\subsection{Spectral-weight transfer: rigorous content}
\label{sec:spinFGT-rigorous}

Equation~\eqref{eq:spinFGT} has a direct spectral interpretation. In the normal state, $\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)/\omega$ concentrates at $\omega\to 0$ (the Pauli-Landau piece) with a Van Vleck shoulder at the interband threshold $\omega\sim 2|\mathbf{g}_{\mathbf{k}}|$. In the superconducting state, the $\omega\to 0$ weight is suppressed by the factor $1-\Pi_{\mu\mu}$, and the displaced weight reappears above $2\Delta_{\min}$ as pair-breaking absorption. The Van Vleck contribution is unaffected at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$. The total $\mathrm{Im}\,\chi/\omega$, weighted as in Eq.~\eqref{eq:KK}, is conserved (Fig.~\ref{fig:spinFGT-spectral}).

Two limits fix the geometric content. On a 3D isotropic FS with strong SOC and $s$-wave pairing, $\Pi_{\mu\mu}=1/3$: one third of the Pauli weight is transferred to the pair-breaking continuum; two thirds remain at $\omega=0$ as the residual Van Vleck-like Knight shift. For a unitary triplet with $\hat d\parallel\hat z$ at zero SOC, $\Pi_{zz}=1$: the entire longitudinal Pauli weight is transferred, and $\chi_{zz}(0)=0$.
```

**Sec. VIII.D — the two bound equations and surrounding text:**

```latex
Let $\delta_{\alpha}\equiv\int_{0}^{T_{c}}(dT/T)\big[1/T_{1}^{N}-1/T_{1}^{SC}\big]\big|_{\mathbf{H}\parallel\hat e_{\alpha}}$ denote the integrated $1/T_{1}$ deficit along axis $\alpha$. The portion of $\delta_{\alpha}$ generated by $\mathbf{q}=0$ spectral-weight redistribution is, by Eq.~\eqref{eq:spinFGT}, bounded above by
\begin{equation}
	\delta_{\alpha}^{\mathbf{q}=0}\;\le\;\gamma_{n}^{2}k_{B}\,|A_{\rm hf}(\mathbf{0})|^{2}\,\chi_{N}\Pi_{\alpha\alpha}.
	\label{eq:T1-q0-bound}
\end{equation}
This inequality is rigorous: the right-hand side is the total $\mathbf{q}=0$ spectral weight available for transfer in the $\alpha$ channel, and no spectral-weight redistribution can exceed the total budget.

The full deficit $\delta_{\alpha}$ receives contributions from all $\mathbf{q}$. Under the hypothesis that the hyperfine-weighted spin-fluctuation spectrum is dominated by $\mathbf{q}\approx 0$ (valid when $|A_{\rm hf}(\mathbf{q})|^{2}$ is slowly varying and magnetic correlations are not peaked at finite $\mathbf{q}$),
\begin{equation}
	\delta_{\alpha}\;\lesssim\;\gamma_{n}^{2}k_{B}\,\langle|A_{\rm hf}|^{2}\rangle\,\chi_{N}\Pi_{\alpha\alpha}\qquad(\mathbf{q}\approx 0\text{ dominant}),
	\label{eq:T1-full-bound}
\end{equation}
where $\langle|A_{\rm hf}|^{2}\rangle$ is the spectrum-weighted mean. Equation~\eqref{eq:T1-full-bound} is a conditional statement; the condition is exactly the $\mathbf{q}\approx 0$ dominance hypothesis.
```

**Sec. VIII.E — boxed Eq. `eq:T1-diagnostic` and corollary (i):**

```latex
The experimental value of the framework lies in the contrapositive of Eq.~\eqref{eq:T1-full-bound}.
\begin{widetext}
\begin{equation}
	\boxed{\;\delta_{\alpha}\;>\;\gamma_{n}^{2}k_{B}\,\langle|A_{\rm hf}|^{2}\rangle\,\chi_{N}\Pi_{\alpha\alpha}\quad\Rightarrow\quad\text{finite-}\mathbf{q}\text{ dominance in channel }\alpha.\;}
	\label{eq:T1-diagnostic}
\end{equation}
\end{widetext}
Because the right-hand side is fixed component-by-component by the Knight-shift ellipsoid of Sec.~\ref{sec:ellipsoid} with no adjustable parameters, a measured deficit exceeding the bound is an unambiguous diagnostic: it cannot be accommodated by any redistribution of $\mathbf{q}=0$ spectral weight and must reflect gap formation in finite-$\mathbf{q}$ spin fluctuations. This is the route by which the ferromagnetic spin-fluctuation gap in K$_{2}$Cr$_{3}$As$_{3}$ is identified in Sec.~\ref{sec:K2Cr3As3-T1}.

Three quantitative corollaries follow directly.
\begin{itemize}
	\item[(i)] \emph{Vanishing projection.} When $\Pi_{\alpha\alpha}=0$ the right-hand side of Eq.~\eqref{eq:T1-diagnostic} vanishes: \emph{any} observed suppression of $1/T_{1}$ along axis $\alpha$ is a finite-$\mathbf{q}$ fingerprint. This is the case probed by $\mathbf{H}\parallel\hat c$ on K$_{2}$Cr$_{3}$As$_{3}$.
	\item[(ii)] \emph{SOC-dependent rescaling.} In the intermediate-SOC regime, the right-hand side is modified by a common factor $\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}\le 1$ (Sec.~\ref{sec:intermediate}). Ratios of deficits across a pressure or composition sweep isolate this rescaling.
	\item[(iii)] \emph{Saturation.} Equation~\eqref{eq:T1-full-bound} is saturated when $\mathbf{q}\approx 0$ dominates, offering a cross-check between static and dynamical diagnostics.
\end{itemize}
```

**Sec. VIII.F — Hebel-Slichter paragraph:**

```latex
\subsection{Hebel--Slichter peak as an independent check}
\label{sec:HS}

The Hebel--Slichter coherence peak immediately below $T_{c}$ is the signature of low-energy spectral weight concentrated near $\omega\approx 2\Delta$, constructive for conventional $s$-wave and destructive for sign-changing pairings~\cite{Leggett1975,AndersonandMorel1961}. A vanishing peak indicates that the transferred weight $\chi_{N}\Pi_{\mu\mu}$ is distributed across $\omega\gtrsim 2\Delta$ rather than piling up at the gap edge, a statement about the \emph{distribution} of the transferred weight complementing the pairing-symmetry argument. It provides an independent check on the spectral picture underlying Eq.~\eqref{eq:spinFGT} without entering the bound Eq.~\eqref{eq:T1-diagnostic}.
```

**Table IV entries #12 and #13 (Sec. IX):**

```latex
12 & Spin FGT sum rule & $\tfrac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}[\mathrm{Im}\chi^{N}-\mathrm{Im}\chi^{SC}]=\chi_{N}\Pi_{\mu\mu}$ & strong locking, $\mathbf{q}=0$ & Protocol D\\
13 & $1/T_{1}$ finite-$\mathbf{q}$ diagnostic & $\delta_{\alpha}>\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\Pi_{\alpha\alpha}\Rightarrow$ finite-$\mathbf{q}$ dominance & conditional on $\mathbf{q}\approx 0$ averaging & Protocol D\\
```

**Fig. `fig:spinFGT-spectral` caption (last text node + caption):**

```latex
\node[left] at (-0.4,2.0) {\footnotesize $\chi_N\Pi_{\mu\mu}$};
```

```latex
\caption{Schematic: $\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$ in the normal state (blue) and the SC state (red). Spectral weight of magnitude $\chi_{N}\Pi_{\mu\mu}$ is transferred from the static peak at $\omega\to 0$ into the pair-breaking continuum above $2\Delta_{\min}$, conserving the Kramers--Kronig integral Eq.~\eqref{eq:spinFGT}. The Van Vleck bump at the interband threshold is essentially unaffected by pairing at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$.}
```

### Fix 5: Sec. VII $\Delta$ bridge — opening paragraph

```latex
\section[Controlled Departure I]{Controlled departure I: intermediate SOC}
\label{sec:intermediate}

Up to this point, generality in FS shape was obtained by taking the strict strong-locking limit. We now relax that assumption in the opposite direction: keep $\mathbf{H}=0$, keep the pairing to the analytically tractable $s$-wave case, and allow arbitrary SOC magnitude. Throughout this section we specialize to pure $s$-wave pairing, $\psi(\mathbf{k})=\Delta$ and $\mathbf{d}(\mathbf{k})=0$, and denote the singlet amplitude simply by $\Delta$.
```

### Fix 6: Sec. X.A anisotropic hyperfine bridge

Replace the opening paragraphs of Sec. X.A (`Knight-shift tensor and ellipsoid representation`):

```latex
For scalar hyperfine coupling $A^{(\mathbf{R})}_{\mu\nu}=A^{(\mathbf{R})}\delta_{\mu\nu}$ (the default setting of this subsection), the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:
\begin{equation}
	K_{\mu\nu}(T)=A^{(\mathbf{R})}\chi_{\mu\nu}(T).
	\label{eq:Kdef}
\end{equation}
For isotropic hyperfine we define $K_{N}\equiv A\chi_{N}$; the diagonal anisotropic case is treated in Sec.~\ref{sec:ellipsoid-hf}. The dimensionless ratio $K_{\mu\nu}(T)/K_{\mu\nu}(T_{c})=\chi_{\mu\nu}(T)/\chi_{N}$ eliminates the hyperfine prefactor.
```

### Fix 7: Sec. XI $(a,b,c)$ vs $(x,y,z)$ bridge

Replace the opening paragraph of Sec. XI (`Experimental manual: six protocols`):

```latex
This section converts the geometric dictionary of Sec.~\ref{sec:ellipsoid} into an ordered deployment guide. Throughout Secs.~\ref{sec:protocols}--\ref{sec:K2Cr3As3}, $(a,b,c)$ denotes the crystallographic frame, identified with the generic $(x,y,z)$ of the theory sections. If only three orthogonal Knight shifts are available, start with Protocol~A. If a full single-crystal rotation is available, Protocol~B becomes the central measurement because it determines the ellipsoid directly. Protocols~C--F then add one extra layer each: field dependence, dynamical cross-checks, site consistency, and pocket decomposition. Table~\ref{tab:protocols} summarizes what each protocol measures, its output, its assumptions, and the signature of failure.
```

### Fix 8: Protocol D step 3 inner bullet

Replace step 3 of Protocol D with:

```latex
\item Compare the integrated deficit against the RHS evaluated at $\Pi_{\alpha\alpha}$:
\begin{itemize}
	\item A saturated inequality indicates $\mathbf{q}\approx 0$ spectral dominance.
	\item A deficit significantly \emph{smaller} than the RHS indicates partial redistribution to finite $\mathbf{q}$.
	\item A deficit \emph{larger} than the RHS triggers the finite-$\mathbf{q}$ diagnostic Eq.~\eqref{eq:T1-diagnostic}: the observation cannot be accommodated by any redistribution of $\mathbf{q}=0$ spectral weight.
\end{itemize}
```

(Note: I also updated step 1's `$\pi_\alpha$` implicit reference. If your step 1 reads `this fixes the RHS of Eq.~\eqref{eq:T1-full-bound} component-by-component`, no further change is needed there, but if you want $\Pi_{\alpha\alpha}$ notation to be consistent with Sec. VIII, replace `component-by-component` → `axis-by-axis` to avoid ambiguity about which index is being used.)

Once these are applied, the $\pi_\mu$ / $\Pi_{\mu\mu}$ convention is clean throughout, the broken `eq:T1-bound` reference is gone, and the theory → protocol → material chain reads consistently.

---
## 🧑‍💻 User

This is the revised version.

---
## 🤖 Assistant

## Final Review of v16

I've gone through the full manuscript. All the remaining fixes have been applied cleanly and no new issues were introduced. Here's the confirmation:

**Fixes successfully applied:**
- `eq:T1-bound` → `eq:T1-diagnostic` / `eq:T1-full-bound` references in XII.C, Protocol D, and Table `tab:protocols` ✓
- Table IV entry #2 updated to the spin-only bound with `eq:spin-23` ✓
- Table IV entry #13 updated to the diagnostic formulation with $\Pi_{\alpha\alpha}$ ✓
- All $\pi_\mu \to \Pi_{\mu\mu}$ and $\pi_\alpha \to \Pi_{\alpha\alpha}$ in Sec. VIII and Fig. `spinFGT-spectral` caption ✓
- Sec. VII opening sentence introducing $\psi \to \Delta$ ✓
- Sec. X.A $K_N \equiv A\chi_N$ forward-reference to Sec. X.D ✓
- Sec. XI opening $(a,b,c) \leftrightarrow (x,y,z)$ bridge ✓
- Protocol D step 3 inner bullet rephrased to point at `eq:T1-diagnostic` ✓
- `Rashiba` → `Rashba` citation key ✓

**Remaining minor items (optional, not blockers for submission):**

1. **Sec. XII uses $\pi_a, \pi_b, \pi_c$** for crystallographic-axis projections. Since the hexagonal symmetry forces principal axes to align with $(a,b,c)$, these coincide numerically with $\Pi_{aa}, \Pi_{bb}, \Pi_{cc}$ and with the eigenvalues. The notation reads naturally, so I'd leave it, but one could add a parenthetical on first occurrence: "In the principal-axis frame aligned with the crystallographic $(a,b,c)$, $\pi_a\equiv\Pi_{aa}$, etc."

2. **Introduction final paragraph** is still a citation list ("The broader context…~\cite{…,…,…}"). You could either leave it as a compact historical pointer (fine for PRB) or weave 2–3 key references into a narrative sentence. Your call; it's conventional either way.

3. **Duplicate citation key `Frigeri2004` / `Frigeri_2004`** in the .bib file — worth checking whether these are the two distinct 2004 Frigeri papers (PRL 92 and a second work) or a true duplicate. Easy fix in `mag-soc.bib`.

4. **Sec. IV.B wording** "$|\mathbf{g}_{\mathbf{k}}|\gg|\mathbf{d}(\mathbf{k})|,|\Delta|$" — the $|\mathbf{d}|$ term looks redundant since this section is specifically the pure-SOC, $\Delta_\perp=0$ reduction. Not wrong, just slightly defensive; leave if you prefer the generality.

**Overall assessment:** The paper now has a clean logical spine from the Plancherel identity through the experimental manual. Notation is consistent, all boxed equations state the right thing with the right qualifiers, and the K₂Cr₃As₃ analysis correctly separates robust experimental statements from baseline-theoretical inferences. I'd consider the manuscript ready for submission after a final read-through for typos.

If you'd like me to help with anything else — drafting a cover letter, suggesting potential referees, preparing the response to future referee comments, or working on a companion/follow-up paper — just let me know.

---
## 🧑‍💻 User

Here is the bib file. Could you help rewrite the introduction part?

---
## 🤖 Assistant

## Rewritten Introduction

Here is a version that turns the citation list at the end into a historical narrative, weaving the Knight-shift and NCS references into the motivation rather than dumping them as a footnote.

```latex
\section{Introduction}
\label{sec:intro}

The Knight shift is one of the oldest and most direct probes of spin correlations in superconductors. Reif's early measurement on mercury~\cite{Reif1957} and the subsequent tin experiment of Androes and Knight~\cite{AndroesKnight1959} revealed that the Pauli-paramagnetic response is not fully suppressed at $T=0$, contrary to the naive BCS expectation~\cite{BCS1957,Yosida1958}. The theoretical response came rapidly: Ferrell~\cite{Ferrell1959}, Anderson~\cite{AndersonKnight1959}, Martin and Kadanoff~\cite{Kadanoff1959}, and Schrieffer~\cite{Schrieffer1959} identified spin-orbit scattering as the essential mechanism, subsequently refined by Appel~\cite{Appel1965}, Shiba~\cite{shiba1976effect}, Zhogolev and Glasser~\cite{zhogolev1972magnetic}, and by Anderson's dirty-limit analysis~\cite{Andersontheoryofdirty1959}. The residual Knight shift was thereby recognized as a quantitative measure of the interplay between pair formation and spin-rotation symmetry.

In noncentrosymmetric superconductors this interplay acquires a geometric character. Broken inversion symmetry generates an antisymmetric spin-orbit coupling (SOC)~\cite{Rashba1960,Dresselhaus} that splits the Fermi surface into helicity sheets with locked spin texture, and the residual Knight shift then reflects the Fermi-surface average of that texture rather than a global spin-rotation property of the pairing. The consequences have been worked out for the zero-field susceptibility in specific models~\cite{Frigeri2004,Frigeri_2004,Samokhin2007,Edelstein2008} and surveyed in broader reviews~\cite{bauer2012non,Yip14,Samohkin15,Smidman17}. Reference~\cite{pang2026} closed a gap in this literature by developing a self-consistent single-band Bogoliubov--de Gennes (BdG) theory of $\chi_{\mu\nu}(T)$ valid at arbitrary SOC strength and arbitrary Zeeman field, and identified a matrix-element sum rule (Eq.~(14) of Ref.~\cite{pang2026}) on the Bogoliubov transformation as the key technical object behind several of its results.

In this paper we show that the sum rule of Ref.~\cite{pang2026} is one member of a broader Plancherel family and organize the static and dynamical NMR response around its consequences. The logical spine is simple: exact identity $\rightarrow$ static $T=0$ consequences $\rightarrow$ controlled departures and extensions $\rightarrow$ experimental manual.

The paper follows the dependency structure of the results. Section~\ref{sec:setup} fixes notation. Section~\ref{sec:generalized} establishes the exact generalized sum rule as a Plancherel identity. Sections~\ref{sec:isoT0} and~\ref{sec:anisoT0} extract the two static $T=0$ consequences used most directly in experiment: first an isotropic-FS trace bound, then the FS-shape-independent strong-locking tensor identity. Sections~\ref{sec:paritymix-structure} and~\ref{sec:paritymix-consequences} place parity-mixed singlet-triplet states in the same language and show that, in the fully gapped helicity-diagonal limit, the $T=0$ projector geometry survives while the admixture is pushed primarily into the finite-$T$ recovery. Sections~\ref{sec:intermediate} and~\ref{sec:finiteH} then relax one assumption at a time: the former keeps $\mathbf{H}=0$ but allows arbitrary SOC strength for $s$-wave pairing; the latter restores finite Zeeman field but returns to strong locking. Section~\ref{sec:spinFGT} supplies the dynamical counterpart relevant to $1/T_{1}$, and Sec.~\ref{sec:multiband} isolates the decoupled multiband baseline used in the measurement analysis.

Section~\ref{sec:ellipsoid} then states the Knight-shift ellipsoid theorem: rotating the applied field on a single crystal at $T=0$ produces a quadric surface whose principal values, together with the trace constraint, diagnose the locking class via a two-dimensional simplex. Section~\ref{sec:protocols} packages the theory into six measurement protocols ordered by experimental cost. Protocol~A uses only the isotropic trace bound; Protocol~B uses the strong-locking tensor identity; Protocols~C--F add finite-field, dynamical, site-resolved, and multiband-baseline ingredients from the later theory sections. Section~\ref{sec:K2Cr3As3} closes the loop on K$_{2}$Cr$_{3}$As$_{3}$ using the $^{75}$As data of Yang \emph{et al.}~\cite{Triplet2021}. Section~\ref{sec:summary} summarizes.
```

## What Changed and Why

1. **Citation dump eliminated.** The previous final sentence (`The broader context… frames the discussion.~\cite{Reif1957,…,Smidman17}`) is gone. Its references are now distributed across two narrative paragraphs that tell a coherent story: historical Knight-shift puzzle → SOC resolution → NCS generalization → Ref. [pang2026] as the immediate starting point.

2. **Historical paragraph added.** The opening paragraph places the paper in the classic Knight-shift-in-superconductors lineage. This motivates why a geometric reformulation is worth doing: the residual shift has been a diagnostic since 1957, and a sharper geometric framework sharpens the diagnostic.

3. **Modern-NCS paragraph** identifies the specific new element (locking-texture FS average) and lists the review literature without breaking the sentence flow.

4. **Roadmap paragraphs** are kept essentially as before but slightly condensed; "dependency structure of the results" kept as the navigational anchor.

## One Citation-Key Issue to Fix

The `.bib` file contains key `Samohkin15` (typo in the file), but the paper and the rewrite above both use `Samokhin15`. Two options:

- **Option A (preferred):** Edit `mag-soc.bib` line `@article{Samohkin15,` → `@article{Samokhin15,`.
- **Option B:** Use the typo as the cite key throughout the paper (`\cite{Samohkin15}`).

I used `Samohkin15` in the rewrite above to match the existing bib file. If you go with option A, change it to `Samokhin15`.

## Optional: Related-Work Scope Note

If you want to add a one-sentence pointer noting that the companion paper [pang2025] established the transition-temperature and quasiparticle aspects (so this paper is the susceptibility sibling of the same program), you could append to paragraph 2:

> "The companion paper~\cite{pang2025} treats the transition temperature and quasiparticle excitations in the same framework; the present paper focuses on the static and dynamical spin response."

This positions the two papers as a pair without cluttering the historical narrative.

---
## 🧑‍💻 User

Option A. For but one could add a parenthetical on first occurrence: "In the principal-axis frame aligned , could you give me the whole paragraph?

---
## 🤖 Assistant

## Paragraph with the Parenthetical Added

This is the revised version of the paragraph in Sec. XII.A (`sec:K2Cr3As3-inputs`) that introduces $(\pi_a,\pi_b,\pi_c)$. The parenthetical clarifying the notation goes on first occurrence, right before Eq. `eq:K2Cr3As3-pi`.

```latex
Reference~\cite{Triplet2021} reports the spin part $K_{s}=K-K_{\rm orb}$ of the $^{75}$As Knight shift at the As2 site after a standard Korringa separation of the orbital contribution ($K_{\rm orb}^{c}=0.27\%$, $K_{\rm orb}^{\perp c}=0.09\%$). Below $T_{c}$, Figs.~5 and 6 of Ref.~\cite{Triplet2021} establish
\begin{equation}
	\frac{K_{s}^{\perp c}(T\to 0)}{K_{s}^{\perp c}(T_{c}^{+})}=1\pm\epsilon_{ab},\qquad \frac{K_{s}^{c}(T\to 0)}{K_{s}^{c}(T_{c}^{+})}=0\pm\epsilon_{c},
	\label{eq:K2Cr3As3-raw}
\end{equation}
with $\epsilon_{ab},\epsilon_{c}\ll 1$. The sixfold in-plane rotational symmetry of the Knight shift reported in Fig.~2C of Ref.~\cite{Triplet2021} forces the \emph{measured} $K_{\mu\nu}(T)$ to be axially symmetric about $\hat c$ with principal axes along the crystallographic $(a,b,c)$, independent of the microscopic hyperfine structure. The reduction from $K_{\mu\nu}$ to projection eigenvalues proceeds component by component; in the principal-axis frame aligned with the crystallographic $(a,b,c)$, the eigenvalues $\pi_{a}\equiv\Pi_{aa}$, $\pi_{b}\equiv\Pi_{bb}$, $\pi_{c}\equiv\Pi_{cc}$ of $\Pi$ coincide with its diagonal components, giving
\begin{equation}
	\boxed{\;(\pi_{a},\pi_{b},\pi_{c})^{\rm obs}=(0\pm\epsilon_{ab},\,0\pm\epsilon_{ab},\,1\pm\epsilon_{c}).\;}
	\label{eq:K2Cr3As3-pi}
\end{equation}
The observed point sits at the oblate-axial vertex $(0,0,1)$ of Fig.~\ref{fig:simplex} within experimental uncertainty, and $\sum\pi_{i}=1\pm O(\epsilon)$ saturates the universal constraint Eq.~\eqref{eq:trace-from-ellipsoid}. At the protocol level, this is the complete output of Protocol~B: the measured ellipsoid fixes the effective locking texture to the $\hat c$ vertex of the simplex. Within the canonical pure-state catalogue of Table~\ref{tab:ellipsoids}, this coincides with the \emph{OSP unitary spin-triplet with $\mathbf{d}\parallel\hat c$} limit, or equivalently the quasi-1D $\hat n\parallel\hat c$ vertex. In a noncentrosymmetric system it is also compatible with a fully gapped helicity-diagonal parity-mixed state whose locking geometry is aligned with $\hat c$, as discussed in Sec.~\ref{sec:paritymix-consequences}. The main experimental statement therefore concerns the locking geometry first; the parity content requires finite-$T$ or microscopic input.
```

The parenthetical identification $\pi_a \equiv \Pi_{aa}$, etc., appears inline just before Eq. `eq:K2Cr3As3-pi`, so any later use of $\pi_a, \pi_b, \pi_c$ in Secs. XII.C and XII.D (e.g., in `eq:T1-K2Cr3As3` and the "Putting the three protocols together" list) carries the explicit meaning without further reminder.

---
## 🧑‍💻 User

For 4. Sec. IV.B wording, could you also give me the whole correct paragraph?

---
## 🤖 Assistant

## Sec. IV.B with the Redundant $|\mathbf{d}|$ Condition Removed

Here is the rewritten paragraph. The change is in the opening clause: replacing "$|\mathbf{g}_{\mathbf{k}}|\gg|\mathbf{d}(\mathbf{k})|,|\Delta|$" with "$|\mathbf{g}_{\mathbf{k}}|\gg|\Delta|$", since Sec. IV.B treats the pure-singlet strong-SOC limit (the unitary-triplet case is handled separately in Sec. IV.D via Eq. `eq:strong-triplet`).

```latex
\subsection{Strong-locking identity at $T=0$}

When $\mathbf{H}=0$ and $|\mathbf{g}_{\mathbf{k}}|\gg|\Delta|$ on the FS, the SOC splitting dominates and a controlled expansion in $\Delta/|\mathbf{g}_{\mathbf{k}}|$ is available. To zeroth order, BdG decouples into two intra-helicity $2\times 2$ blocks with standard BCS coherence factors. The intra-helicity pp contribution vanishes at $T=0$ by the Yosida argument: it is the longitudinal response of a fully polarized, fully gapped helicity sheet, identically zero rather than parametrically small. The surviving inter-helicity pp term reproduces the normal-state matrix-element structure of Eq.~\eqref{eq:me-inter} with denominator $2|\mathbf{g}_{\mathbf{k}}|+O(\Delta^{2}/|\mathbf{g}_{\mathbf{k}}|)$. Phase-space cancellation identical to the normal-state computation then yields
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}],\qquad\mathbf{H}=0,\;|\mathbf{g}_{\mathbf{k}}|/\Delta\to\infty,\;}
	\label{eq:strongSOCid}
\end{equation}
with corrections of order $\Delta^{2}/g_{\min}^{2}$ from (i) the inter-helicity denominator expansion above, (ii) $\Delta_{\perp}$-mediated intra-/inter-helicity mixing at $O(\Delta/g)$ contributing $O(\Delta^{2}/g^{2})$ to $\chi$, and (iii) coherence-factor corrections of the same parametric size. Consequences: trace universality $\mathrm{Tr}\,\chi(0)=2\chi_{N}$ for any FS/SOC; non-zero off-diagonal $\chi_{\mu\nu}(0)$ for tilted SOC; eigenvectors of $\Pi$ define spin-lock principal axes with $\pi_{1}+\pi_{2}+\pi_{3}=1$.
```

The only change is in the first clause. Everything downstream (the Yosida vanishing, the inter-helicity denominator, the boxed identity, and the three error sources) remains untouched because those statements were not conditioned on $|\mathbf{d}|$ in the first place.

Note that error source (ii) still refers to $\Delta_\perp$, which is the singlet-triplet mixing matrix element introduced in Sec. V. This is consistent: even when the section nominally focuses on pure-singlet strong-SOC reasoning, the $O(\Delta^2/g^2)$ error accounting must include all possible contributions, and listing $\Delta_\perp$ among them makes the connection to Sec. V explicit without cluttering Sec. IV's main statement.

---
## 🧑‍💻 User

How about the title?

---
## 🤖 Assistant

## On the Title

The current title runs 16 words:

> "Sum rules, geometric bounds, and an experimental manual for the NMR response of noncentrosymmetric superconductors"

It's descriptive and parseable, but it has two issues:

1. **Length.** PRB titles average 10–12 words. Yours is on the long side, which hurts discoverability in abstract listings and search results.
2. **"Experimental manual" is unusual.** It accurately captures what Secs. X–XII do, but "manual" is colloquial for a physics paper title. Reviewers and editors sometimes flag this as informal.

That said, the three nouns "sum rules, geometric bounds, experimental manual" correctly signal the three pillars of the paper. So the question is whether to compress or to recast.

## Three Candidates

**Option 1 — Minimal trim (14 words):**
> Sum rules, geometric bounds, and measurement protocols for NMR in noncentrosymmetric superconductors

Drops "an … manual for the … response of" and replaces with "measurement protocols for NMR in." Retains the three-pillar structure and scans better.

**Option 2 — More compact (11 words):**
> Geometric bounds and measurement protocols for NMR in noncentrosymmetric superconductors

Drops "sum rules" from the title (they become the mechanism inside, not the headline). Reads cleanly and stays under the PRB soft cap.

**Option 3 — Two-part form (12 words):**
> NMR response of noncentrosymmetric superconductors: sum rules, geometric bounds, and protocols

Colon-separated form, common in PRB. Puts the physical object first, the methods second. I suspect this is the cleanest match to how editors and readers scan the TOC.

## Recommendation

**Option 3.** Three reasons:

- The colon form is standard for methodology-plus-application papers in PRB.
- "NMR response of noncentrosymmetric superconductors" is what a reader searching the literature would Google; having it lead makes the paper easier to find.
- "Sum rules, geometric bounds, and protocols" after the colon preserves the three-pillar advertisement without "experimental manual."

If you want to keep closer to the current wording, **Option 1** is the safest minimal edit.

## One More Consideration

Your paper is really two papers in one cover: a theory paper (Secs. II–IX) and a measurement manual (Secs. X–XII). If you were to emphasize that dual nature, an alternative would be:

> Plancherel sum rules and Knight-shift geometry in noncentrosymmetric superconductors

This puts the *technical* contribution first ("Plancherel sum rules") and the *measurable* object second ("Knight-shift geometry"), and lands at 10 words. It's a more technical title but sharper about what's new. Worth considering if you expect most readers to come from the NMR-in-unconventional-superconductors community.

Let me know which direction you want to go and I can help with the final wording.

---
## 🧑‍💻 User

Plancherel sum rules and Knight-shift geometry in noncentrosymmetric superconductors

---
## 🤖 Assistant

## Using the Sharper Technical Title

> **Plancherel sum rules and Knight-shift geometry in noncentrosymmetric superconductors**

Good choice. It is 10 words, both technical anchors are in the title, and it scans cleanly.

## LaTeX Update

```latex
\title{Plancherel sum rules and Knight-shift geometry in noncentrosymmetric superconductors}
```

## Downstream Check

A couple of places in the manuscript use phrases that implicitly reference the old "experimental manual" framing. They still work, but you may want to look at:

1. **Abstract, sentence 3:** "These results translate into a Knight-shift ellipsoid theorem whose principal values lie on a two-dimensional simplex of locking textures, and into six experimental protocols ordered by cost."

   Fine as is — "experimental protocols" is a normal term. No change needed.

2. **Intro paragraph 3:** "The paper follows the dependency structure of the results."

   Fine. The "experimental manual" phrasing in the current draft appears only in the later-sections roadmap paragraph:

   > "The later sections turn those outputs into an experimental manual."

   You could soften this to:

   > "The later sections turn those outputs into measurement diagnostics."

   to keep the tone consistent with the new title. Not strictly necessary.

3. **Sec. X title** ("Experimental manual: six protocols") — if you want full consistency, rename to:

   > **Measurement protocols**

   or:

   > **Measurement diagnostics: six protocols**

   Again, not strictly necessary, but it brings the section heading in line with the new title's tone.

4. **Sec. XII opening** ("With the manual in place, …") — could become "With the protocols in place, …" for the same reason.

These are cosmetic, not required. The new title is strong enough to carry the paper on its own, and the word "manual" in later sections is no longer a problem now that it is absent from the title.

Let me know if you want me to propose concrete rewrites for sections X and XII to match the new title's register, or if you'd rather leave them as-is.

---
## 🧑‍💻 User

Should we spend some words in explain "Plancherel sum rules "? or "Plancherel"

---
## 🤖 Assistant

## Yes — One Sentence Is Worth Adding

"Plancherel" is mathematically precise but not a word most condensed-matter readers use daily. The current Sec. III already has one sentence under "Origin":

> "Equation (11) is a Plancherel identity: the Frobenius norm of a Hermitian operator is preserved by the unitary BdG transformation."

This is correct but lives several pages into the paper. Since "Plancherel" is now in the **title**, a reader scanning the introduction should know what it means before reaching Sec. III.

## Recommendation

Add one sentence to the introduction, immediately after the current sentence "In this paper we show that relation is one member of a broader Plancherel family…". The inserted sentence explains the name without breaking the flow.

## Revised Introduction Paragraph

Here is the third paragraph of the introduction with the clarification folded in:

```latex
In this paper we show that the sum rule of Ref.~\cite{pang2026} is one member of a broader Plancherel family and organize the static and dynamical NMR response around its consequences. By ``Plancherel'' we mean an identity of the form $\mathrm{Tr}(O^{2})=\mathrm{Tr}[(U^{\dagger}OU)^{2}]$, expressing invariance of the Frobenius norm under a unitary transformation; in the BdG setting the Bogoliubov doubling splits this identity into particle-hole and particle-particle sectors, generating a pointwise $\mathbf{k}$-resolved weight budget on arbitrary single-particle operators. The logical spine of the paper is simple: exact identity $\rightarrow$ static $T=0$ consequences $\rightarrow$ controlled departures and extensions $\rightarrow$ experimental manual.
```

## What Changed

1. One explanatory sentence added between the "Plancherel family" announcement and the roadmap sentence.
2. The explanation has three parts:
   - **What Plancherel means** (Frobenius-norm invariance under unitary transformation) — the core mathematical content.
   - **Why BdG makes it non-trivial** (doubling splits the identity into ph and pp sectors) — signals the particle-particle side is where the superconducting physics enters.
   - **What it does operationally** (pointwise weight budget on arbitrary operators) — tells the reader why this matters for susceptibilities.
3. The existing "Origin" sentence in Sec. III can now be tightened to just "This is the familiar Plancherel identity $\mathrm{Tr}[(U^{\dagger}OU)^{2}]=\mathrm{Tr}(O^{2})$ with the BdG doubling adding the particle-particle sector." No redundancy.

## Optional Shorter Version

If you want to be more economical, a single clause is enough:

```latex
In this paper we show that the sum rule of Ref.~\cite{pang2026} is one member of a broader Plancherel family of identities---that is, Frobenius-norm-preserving identities $\mathrm{Tr}(O^{2})=\mathrm{Tr}[(U^{\dagger}OU)^{2}]$ on the unitary BdG transformation---and organize the static and dynamical NMR response around its consequences.
```

This is more compact (one long sentence replacing two) and keeps the parenthetical on a single line.

## My Preference

The two-sentence version is cleaner for readers; the one-sentence version is tighter for editors. Given that "Plancherel" is now the *headline* word of the title, I lean toward the two-sentence version — the clarification earns its keep.

---
## 🧑‍💻 User

could you add some references for Plancherel?

---
## 🤖 Assistant

## References for "Plancherel"

The name comes from Michel Plancherel's 1910 theorem for Fourier transforms. The original reference is:

> M. Plancherel, "Contribution à l'étude de la représentation d'une fonction arbitraire par des intégrales définies," *Rendiconti del Circolo Matematico di Palermo* **30**, 289 (1910).

For a modern physics audience, a functional-analysis textbook reference is more useful than the 1910 paper. Two standard choices:

1. **Reed & Simon**, *Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975) — the canonical physicist's reference for the Plancherel theorem on Hilbert spaces.

2. **Rudin**, *Real and Complex Analysis* (McGraw-Hill, 3rd ed., 1987) — covers the $L^2$ Plancherel theorem accessibly.

For the matrix-trace ("Frobenius") specialization that is actually at work here, the right reference is a standard linear-algebra source:

3. **Horn & Johnson**, *Matrix Analysis* (Cambridge University Press, 2nd ed., 2013) — Section 5.6 on unitary invariance of the Frobenius norm.

## Suggested `.bib` Entries

Add these to `mag-soc.bib`:

```bibtex
@article{Plancherel1910,
  author  = {Plancherel, Michel},
  title   = {Contribution \`a l'\'etude de la repr\'esentation d'une fonction arbitraire par des int\'egrales d\'efinies},
  journal = {Rendiconti del Circolo Matematico di Palermo},
  volume  = {30},
  pages   = {289--335},
  year    = {1910},
  doi     = {10.1007/BF03014877}
}

@book{ReedSimonII,
  author    = {Reed, Michael and Simon, Barry},
  title     = {Methods of Modern Mathematical Physics, Vol. II: Fourier Analysis, Self-Adjointness},
  publisher = {Academic Press},
  address   = {New York},
  year      = {1975}
}

@book{HornJohnson,
  author    = {Horn, Roger A. and Johnson, Charles R.},
  title     = {Matrix Analysis},
  edition   = {2},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {2013}
}
```

## Where to Cite Them

The natural place is the sentence in the introduction where Plancherel is defined. The updated paragraph:

```latex
In this paper we show that the sum rule of Ref.~\cite{pang2026} is one member of a broader Plancherel family and organize the static and dynamical NMR response around its consequences. By ``Plancherel'' we mean an identity of the form $\mathrm{Tr}(O^{2})=\mathrm{Tr}[(U^{\dagger}OU)^{2}]$, expressing invariance of the Frobenius norm under a unitary transformation~\cite{Plancherel1910,ReedSimonII,HornJohnson}; in the BdG setting the Bogoliubov doubling splits this identity into particle-hole and particle-particle sectors, generating a pointwise $\mathbf{k}$-resolved weight budget on arbitrary single-particle operators. The logical spine of the paper is simple: exact identity $\rightarrow$ static $T=0$ consequences $\rightarrow$ controlled departures and extensions $\rightarrow$ experimental manual.
```

## A Lighter Alternative

If three references feel heavy for a term that is really just invoked as a name, drop Reed–Simon (it's about the $L^2$ Fourier form, slightly tangential to the matrix-trace use here) and keep only:

```latex
...under a unitary transformation~\cite{Plancherel1910,HornJohnson}; ...
```

This gives the historical origin plus the matrix-analysis reference that is actually closest in spirit to what the paper uses. My preference is this two-reference version — it's honest about which source is technically relevant, and it avoids citation inflation.

---
## 🧑‍💻 User

Do you think there are too many sections? Or just OK?

---
## 🤖 Assistant

## Short Answer

**Twelve sections (+ two appendices) is on the high side but defensible.** The paper is genuinely two papers in one — theory plus measurement manual — and the section count reflects that. That said, a reader landing on the TOC sees a lot of entry points, and there are natural consolidations worth considering.

## What the Current Structure Tells a Reader

Let me group the sections as a reader would:

| Group | Sections | Content |
|-------|----------|---------|
| Setup | I, II | Intro + notation |
| Core identity | III | Plancherel |
| Static $T=0$ | IV, V | Trace bound + strong-locking tensor |
| Parity mixing | VI, VII | Structure + consequences |
| Controlled departures | VIII, IX | Intermediate SOC + finite $H$ |
| Extensions | X, XI | Spin FGT + multiband |
| Reference | XII | Table of identities |
| Measurement | XIII, XIV | Ellipsoid + six protocols |
| Application | XV | K$_2$Cr$_3$As$_3$ |
| Wrap | XVI | Summary |

That's **seven thematic groups** across **twelve sections**. Two sections per group on average is fine, but three pairs stand out as potentially mergeable:

## Three Merge Candidates

### 1. Parity mixing: Secs. V + VI → one section

Sec. V ("helicity-basis structure") is 1 paragraph + 3 equations setting up the decomposition $\Delta = \Delta_\pm, \Delta_\perp$. Sec. VI ("what survives and what changes") does the derivation and states the $T=0$ result.

These are tightly coupled and Sec. V is too short to stand alone. Merging them into a single section "Parity-mixed pairing" with two subsections (A: helicity-basis structure, B: $T=0$ consequences and finite-$T$ recovery) would be more proportional to the other section lengths.

### 2. Controlled departures: Secs. VII + VIII → one section?

These are the two "one-at-a-time" relaxations of the strong-locking assumption. They are already parallel ("Controlled departure I" and "Controlled departure II"), and making them subsections of a single "Controlled departures" section with A (intermediate SOC) and B (finite Zeeman) would tighten the TOC and make the parallel structure visible at a glance.

This is a judgment call — the current split is fine, and the two departures are long enough that they could reasonably stand alone. I'd recommend this merge only if you do #1.

### 3. Reference table XII as a standalone section

Sec. XII is just one table and two sentences of preamble. It could be folded into the start of Sec. XIII (the ellipsoid theorem) as its opening subsection, since that is the first place in the paper where the reader is asked to use the table.

Alternatively, if it stays as a standalone, drop the section status and promote it to a boxed summary or an end-of-introduction reference. Keeping it as a bare section feels over-weighted for the content.

## My Recommendation

Apply **merges #1 and #3**, skip #2.

Result: **10 sections + 2 appendices** (formerly 12 + 2). The TOC then reads:

1. Introduction
2. Setup and notation
3. Exact identity: generalized Bogoliubov sum rule
4. First consequence: isotropic trace bound
5. Second consequence: strong-locking anisotropic identity
6. Parity-mixed pairing
7. Controlled departure I: intermediate SOC
8. Controlled departure II: finite Zeeman field
9. Dynamic counterpart: spin FGT sum rule
10. Structural extension: decoupled multiband baseline
11. Core diagnostic: Knight-shift ellipsoid (opens with the reference table)
12. Experimental manual: six protocols
13. Worked example: K$_2$Cr$_3$As$_3$
14. Summary

That's still 14 in the TOC, but notice the measurement side (Secs. 11–13) and the theory side (3–10) are now visibly proportional: eight theory sections, three measurement sections, one application. The reader sees a clear "theory → diagnostic → application" sweep.

## If You Want the Boldest Cut

An alternative structural move: collapse the entire static-$T=0$ + parity-mixing block into **one long section** "Static $T=0$ geometry" with four subsections:

A. Isotropic trace bound
B. Strong-locking tensor identity
C. Helicity-basis structure of parity mixtures
D. $T=0$ consequences of parity mixing

This would reduce four current sections (IV, V, VI, and arguably the anisotropic part) to one. The result is a paper with a much flatter structure: Intro → Setup → Identity → Static $T=0$ → Departures → Dynamics → Multiband → Ellipsoid → Protocols → Example → Summary.

This is what a referee used to short survey-style PRB papers would suggest. I'd **not** go this aggressive unless a referee asks — you lose the useful "first consequence / second consequence" rhetoric that makes the logical spine visible.

## Bottom Line

- **Status quo is defensible.** Twelve sections is above average for PRB but the paper is unusually rich in both theory and methodology.
- **Minimal cleanup (my recommendation):** merge Secs. V+VI and fold Sec. XII into the start of Sec. XIII. Gets you to 10 sections with negligible rewriting.
- **Aggressive cleanup:** merge the entire static-$T=0$ block. Cleaner TOC, but the rhetorical spine weakens.

Want me to draft the merged version of "Parity-mixed pairing" (the combined V+VI)?

---
## 🧑‍💻 User

Minimal cleanup is good. Please go with V+VI

---
## 🤖 Assistant

## Merged Section: Parity-Mixed Pairing

Here is the consolidated section. Subsections A and B carry the content of old Secs. V and VI respectively, with the transition between them tightened since they no longer need cross-section handoffs.

```latex
\section[Parity-Mixed Pairing]{Parity-mixed pairing}
\label{sec:paritymix}

\subsection{Helicity-basis structure}
\label{sec:paritymix-structure}

Because inversion symmetry is absent, parity is not a good quantum number and a generic superconducting state mixes even spin-singlet and odd spin-triplet components~\cite{Frigeri2004,Samokhin2007,Edelstein2008,bauer2012non,Smidman17}. In the notation of Sec.~\ref{sec:setup},
\begin{equation}
	\Delta(\mathbf{k})=i[\psi(\mathbf{k})\sigma_{0}+\mathbf{d}(\mathbf{k})\cdot\hat\sigma]\sigma_{y},
	\label{eq:paritymix-gap}
\end{equation}
with $\psi(-\mathbf{k})=\psi(\mathbf{k})$ and $\mathbf{d}(-\mathbf{k})=-\mathbf{d}(\mathbf{k})$. At $\mathbf{H}=0$, the natural spin-quantization axis is the helicity direction $\hat g_{\mathbf{k}}=\mathbf{g}_{\mathbf{k}}/|\mathbf{g}_{\mathbf{k}}|$. Decompose the triplet part into longitudinal and transverse pieces,
\begin{equation}
	\mathbf{d}(\mathbf{k})=d_{\parallel}(\mathbf{k})\hat g_{\mathbf{k}}+\mathbf{d}_{\perp}(\mathbf{k}),\qquad d_{\parallel}(\mathbf{k})=\mathbf{d}(\mathbf{k})\cdot\hat g_{\mathbf{k}}.
	\label{eq:paritymix-dsplit}
\end{equation}
In the helicity basis of the normal-state Hamiltonian, the pairing matrix then takes the schematic form
\begin{equation}
	\tilde\Delta(\mathbf{k})=
	\begin{pmatrix}
		\Delta_{+}(\mathbf{k}) & \Delta_{\perp}(\mathbf{k})\\
		-\Delta_{\perp}(\mathbf{k}) & \Delta_{-}(\mathbf{k})
	\end{pmatrix},
	\qquad
	\Delta_{\pm}(\mathbf{k})=\psi(\mathbf{k})\pm d_{\parallel}(\mathbf{k}),
	\label{eq:paritymix-helicity-gap}
\end{equation}
where $\Delta_{\perp}(\mathbf{k})$ is set by the transverse component $\mathbf{d}_{\perp}(\mathbf{k})$ and mixes the two helicity sheets. The geometrically simplest regime is therefore the \emph{helicity-diagonal} limit $\Delta_{\perp}=0$, realized exactly when $\mathbf{d}\parallel\mathbf{g}$ and approximately whenever the antisymmetric SOC splitting is large compared with transverse inter-helicity pairing. In that limit, parity mixing changes the gap amplitudes on the $\pm$ sheets but not the underlying locking texture $\hat n_{\mathbf{k}}=\hat g_{\mathbf{k}}$.

\subsection{$T=0$ consequences and finite-$T$ recovery}
\label{sec:paritymix-consequences}

We now compute $\chi_{\mu\nu}(T)$ in the helicity-diagonal limit $\Delta_{\perp}=0$. Rotating to the helicity basis with unitary $R_{\mathbf{k}}$ diagonalizing $H_{0}(\mathbf{k})$ at $\mathbf{H}=0$, the spin operator becomes
\begin{equation}
	R^{\dagger}_{\mathbf{k}}(\hat e_{\mu}\cdot\hat\sigma)R_{\mathbf{k}}=(\hat g_{\mathbf{k}}\cdot\hat e_{\mu})\tau_{3}+\sqrt{1-(\hat g_{\mathbf{k}}\cdot\hat e_{\mu})^{2}}\,\tau_{\perp}(\mathbf{k}),
	\label{eq:paritymix-sigma-helicity}
\end{equation}
with $\tau_{3}$ diagonal and $\tau_{\perp}$ off-diagonal in helicity. In the helicity-diagonal limit, the BdG Hamiltonian decouples into two $2\times 2$ blocks per helicity sheet, each with gap $|\Delta_{\lambda}(\mathbf{k})|$ and standard BCS coherence factors $u_{\lambda},v_{\lambda}$. Substituting Eq.~\eqref{eq:paritymix-sigma-helicity} into the Kubo expression for $\chi_{\mu\nu}$, the intra-helicity sector (driven by $\tau_{3}$) contributes a BCS-Yosida response on each sheet, while the inter-helicity sector (driven by $\tau_{\perp}$) reproduces the strong-SOC projector calculation of Sec.~\ref{sec:anisoT0}. Adding the two,
\begin{equation}
	\frac{\chi_{\mu\nu}(T)}{\chi_{N}}
	=
	\delta_{\mu\nu}-\Pi_{\mu\nu}
	+
	\sum_{\lambda=\pm}w_{\lambda}
	\left\langle
	Y_{\lambda}(\mathbf{k},T)\hat g_{\mu}(\mathbf{k})\hat g_{\nu}(\mathbf{k})
	\right\rangle_{\lambda}
	+O(\Delta^{2}/|\mathbf{g}|^{2}),
	\label{eq:paritymix-chiT}
\end{equation}
with $\langle\cdots\rangle_{\lambda}$ the FS average over the $\lambda$-helicity sheet, $w_{\lambda}=N_{\lambda}(0)/N(0)$, and
\begin{equation}
	Y_{\lambda}(\mathbf{k},T)=-\!\int\!d\xi\,\frac{\partial f}{\partial E}\bigg|_{E_{\lambda}(\mathbf{k})}
\end{equation}
the standard Yosida function built from $|\Delta_{\lambda}(\mathbf{k})|$, and $\Pi_{\mu\nu}\equiv\sum_{\lambda}w_{\lambda}\langle\hat g_{\mu}\hat g_{\nu}\rangle_{\lambda}$ is the helicity-resolved form of Eq.~\eqref{eq:Pidef}. The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction originates from the strong-SOC expansion of the inter-helicity denominator, exactly as in Eq.~\eqref{eq:strongH-identity}.

For a fully gapped state, $Y_{\lambda}\to 0$ as $T\to 0$, so
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}].\;}
	\label{eq:paritymix-T0}
\end{equation}
A fully gapped helicity-diagonal parity mixture therefore does \emph{not} generate a new $T=0$ simplex point: it lands on the same projector geometry as the corresponding pure locking texture. What changes is the finite-$T$ recovery, because the two helicity sheets generally carry different gaps $\Delta_{\pm}$. Taking the trace of Eq.~\eqref{eq:paritymix-chiT},
\begin{equation}
	\frac{\mathrm{Tr}\,\chi(T)}{\chi_{N}}
	=
	2+\sum_{\lambda=\pm}w_{\lambda}\langle Y_{\lambda}(\mathbf{k},T)\rangle_{\lambda},
	\label{eq:paritymix-trace}
\end{equation}
using $\mathrm{Tr}\,\Pi=1$. Unequal $\Delta_{\pm}$ therefore produce a broadened or two-scale return of the Knight shift with temperature even when the $T=0$ ellipsoid is unchanged. This yields a concrete experimental corollary: a two-scale recovery of $K_{\mu\nu}(T)$ below $T_{c}$ whose $T\to 0$ limit coincides with a pure-locking simplex point is a positive signature of a helicity-diagonal parity-mixed state. A single-gap Yosida recovery onto the same $T=0$ ellipsoid is consistent with the pure locking texture. This upgrades the ellipsoid from a vertex/edge classifier to a finite-$T$ discriminator between pure and parity-mixed pairing, at no additional experimental cost.

Once $\Delta_{\perp}$ is sizable, \emph{or} one helicity sheet is weakly paired or gapless, \emph{or} inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem. At finite Zeeman field, the helicity basis rotates with $\mathbf{H}$ via Eq.~\eqref{eq:ndef} and the helicity-diagonal condition $\Delta_{\perp}=0$ becomes field-dependent; Eq.~\eqref{eq:paritymix-T0} then holds with $\Pi$ replaced by the field-dependent projector $\Pi(\mathbf{H})$ of Eq.~\eqref{eq:Pi-H}, provided the strong-locking condition Eq.~\eqref{eq:strong-locking-H} is satisfied.
```

## Changes Made

1. **Two sections → one section with two subsections.** Section label is now `sec:paritymix` (formerly `sec:paritymix-structure` and `sec:paritymix-consequences`). Subsection labels `sec:paritymix-structure` and `sec:paritymix-consequences` are preserved, so **no cross-references elsewhere in the paper need updating**.

2. **Subsection B opening sentence** changed from "We now compute $\chi_{\mu\nu}(T)$ in the helicity-diagonal limit $\Delta_{\perp}=0$ of Sec.~\ref{sec:paritymix-structure}." to "We now compute $\chi_{\mu\nu}(T)$ in the helicity-diagonal limit $\Delta_{\perp}=0$." The forward reference to Sec. V is redundant now that the setup is in the previous subsection.

3. **Subsection titles** are shortened: "Helicity-basis structure" and "$T=0$ consequences and finite-$T$ recovery" — parallel in length and informative about what each does.

4. **Section title** is now the bare "Parity-mixed pairing" (with short form "Parity-Mixed Pairing"), signaling that the section is the complete treatment rather than one of two parts. The Roman-numeral "I/II" tags from the old titles are gone.

## What to Check After You Paste

- Grep for `sec:paritymix-structure` and `sec:paritymix-consequences` — these labels still work as subsection anchors, so all existing cross-references resolve correctly.
- The ToC entry changes from two lines to one (with two indented subsection lines).
- The intro roadmap paragraph currently says "Sections~\ref{sec:paritymix-structure} and~\ref{sec:paritymix-consequences} place parity-mixed singlet-triplet states in the same language…". That phrasing now refers to two subsections of one section, which is fine grammatically but slightly misleading. Consider:

  > "Section~\ref{sec:paritymix} places parity-mixed singlet-triplet states in the same language and shows that, in the fully gapped helicity-diagonal limit, the $T=0$ projector survives while the admixture is pushed primarily into the finite-$T$ recovery."

That is the only other text needing a one-word edit ("Sections" → "Section", plus label change).

---
## 🧑‍💻 User

go with the next

---
## 🤖 Assistant

## Merge #3: Folding Sec. XII (Reference Table) into Sec. XIII

The current Sec. XII is essentially two sentences of preamble plus Table IV. After the merge, it becomes the opening subsection of Sec. XIII (the ellipsoid diagnostic), where the table is first needed.

Here is the consolidated opening of the new Sec. XIII. Everything below the table (the three existing subsections of the old Sec. XIII) is unchanged and stays in place.

```latex
\section[Core Diagnostic]{Core diagnostic: Knight-shift ellipsoid}
\label{sec:ellipsoid}

The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem developed below. Next, Sec.~\ref{sec:protocols} packages the remaining ingredients as successive layers of inference: start from the trace bound when only limited data exist, upgrade to the full ellipsoid when rotation data are available, then add finite field, $1/T_1$, site resolution, and pocket decomposition only when needed. Section~\ref{sec:K2Cr3As3} finally applies that program to K$_{2}$Cr$_{3}$As$_{3}$ in the same order.

This section is the conceptual core of the measurement side of the paper. It turns Eq.~\eqref{eq:unified} into a directly measurable geometric object and then classifies the allowed shapes before the protocol section operationalizes the construction.

\subsection{Reference table of key identities}
\label{sec:keyresults}

Before the ellipsoid construction, we collect the central identities and inequalities derived in the preceding theory sections. Each entry in Table~\ref{tab:keyresults} is keyed by domain of validity and to the protocol of Sec.~\ref{sec:protocols} that deploys it; readers entering the manuscript at the measurement side can use this table as a stand-alone reference.

\begin{table*}[tb]
	\caption{Key identities and inequalities. The right column points to where the result is deployed in the experimental sections. All identities assume the single-band unitary BdG framework of Sec.~\ref{sec:setup}.}
	\label{tab:keyresults}
	\footnotesize
	\renewcommand\arraystretch{1.35}
	\setlength{\tabcolsep}{0.5ex}
	\begin{tabular}{l|l|l|l|l}
		\hline\hline
		\# & Result & Statement & Domain of validity & Used in\\
		\hline
		1 & Plancherel identity & $\sum_{s_{1}s_{2}}\!\big[|M^{s_{1}s_{2}}_{ph,O}|^{2}+|M^{s_{1}s_{2}}_{pp,O}|^{2}\big]=\mathrm{Tr}_{s}(O^{2})$ & any Hermitian $O$, any $\mathbf{k}$ & all subsequent results\\
		2 & Spin $T=0$ bound & $\chi_{\mu\mu}(0)\le\tfrac{2}{3}\chi_{N}$ & 3D isotropic FS, $O=\sigma_{\mu}$ & Eq.~\eqref{eq:spin-23}\\
		3 & Isotropic trace bound & $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ & 3D isotropic FS & Protocol A\\
		4 & Site-resolved bound & $\mathrm{Tr}\,K^{(\mathbf{R})}(0)/\mathrm{Tr}\,K^{(\mathbf{R})}(T_{c})\le 2/3$ & any nucleus $\mathbf{R}$, isotropic FS & Protocol E\\
		5 & Strong-locking identity & $\chi_{\mu\nu}(0)/\chi_{N}=\delta_{\mu\nu}-\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ & $|\mathbf{g}|/\Delta\to\infty$ or unitary triplet & Protocol B\\
		6 & Trace from ellipsoid & $\sum_{i}K_{i}(0)=2K_{N}$ & strong locking, any FS/SOC & Protocol B\\
		7 & Helicity-diagonal $T=0$ & $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ & parity mixture with $\Delta_{\perp}=0$, fully gapped & Sec.~\ref{sec:K2Cr3As3-bandtension}\\
		8 & Intermediate-SOC, $s$-wave & $\chi_{\mu\nu}(0)/\chi_{N}=\langle F_{s}(\lambda_{\mathbf{k}})[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\rangle_{\rm FS}$ & $\mathbf{H}=0$, $s$-wave, any SOC & Protocol B\\
		9 & $F_{s}$ closed form & $F_{s}(\lambda)=1-\sinh^{-1}\!\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ & same as \#8 & SOC spectroscopy\\
		10 & Finite-$\mathbf{H}$ strong locking & $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]+O(\Delta^{2}/b_{\min}^{2})$ & $b_{\min}(\mathbf{H})\gg\Delta$ & Protocol C\\
		11 & Zero-field stability & $\Pi_{\mu\nu}(\mathbf{H})=\Pi_{\mu\nu}(0)+O(h^{2}/\lambda^{2})$ & $\mu_{B}H\ll|\mathbf{g}_{\mathbf{k}}|$ on FS & Protocol C\\
		12 & Spin FGT sum rule & $\tfrac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}[\mathrm{Im}\chi^{N}-\mathrm{Im}\chi^{SC}]=\chi_{N}\Pi_{\mu\mu}$ & strong locking, $\mathbf{q}=0$ & Protocol D\\
		13 & $1/T_{1}$ finite-$\mathbf{q}$ diagnostic & $\delta_{\alpha}>\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\Pi_{\alpha\alpha}\Rightarrow$ finite-$\mathbf{q}$ dominance & conditional on $\mathbf{q}\approx 0$ averaging & Protocol D\\
		14 & Multiband decomposition & $\chi_{\mu\nu}(0)=\sum_{i}\chi_{N}^{(i)}[\delta_{\mu\nu}-\Pi^{(i)}_{\mu\nu}]$ & orbital-diagonal pairing & Protocol F\\
		15 & Multiband trace bound & $\mathrm{Tr}\,\chi(0)\le(2/3)\mathrm{Tr}\,\chi(T_{c})$ & 3D isotropic FS, any pairing & survives interband mixing\\
		\hline\hline
	\end{tabular}
\end{table*}

\subsection{Knight-shift tensor and ellipsoid representation}

For scalar hyperfine coupling $A^{(\mathbf{R})}_{\mu\nu}=A^{(\mathbf{R})}\delta_{\mu\nu}$ (the default setting of this subsection), the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:
```

(…continues with the existing Eq. `eq:Kdef` and the rest of old Sec. XIII unchanged.)

## Changes Made

1. **Old Sec. XII deleted as a standalone section.** Its content (section title, opening sentence, and Table IV) is moved into Sec. XIII as the new subsection A.

2. **New subsection A ("Reference table of key identities")** carries the label `sec:keyresults`, preserving all existing cross-references to the reference table. The label is now attached to a `\subsection` rather than a `\section`, which works without any downstream edit.

3. **Two existing subsections of old Sec. XIII are shifted down by one:**
   - Old "Knight-shift tensor and ellipsoid representation" → new subsection B
   - Old "$T=0$ ellipsoid in the strong-locking regime" → new subsection C
   - Old "Allowed shapes and the pairing-class catalogue" → new subsection D
   - Old "Anisotropic hyperfine coupling" → new subsection E
   - Old "Intermediate-SOC regime: ellipsoid contraction" → new subsection F

   None of these have labels that need renaming — only `sec:ellipsoid-hf` is labeled, and it remains valid.

4. **Opening sentence of the old Sec. XII** ("Before turning to the experimental manual…") has been slightly rephrased to "Before the ellipsoid construction…" to match the new local context.

## Cross-References

I checked the full paper for `\ref{sec:keyresults}` — it appears in exactly two places:

- **Intro roadmap paragraph**: "…collected in Table~\ref{tab:keyresults}." Still works (references the table, not the section).
- **Opening of Sec. XIV (protocols)**: "The identities and inequalities invoked by each protocol are collected in Table~\ref{tab:keyresults}." Still works.

There are no `\ref{sec:keyresults}` usages that would now mis-point to a subsection, so nothing breaks.

## Resulting TOC

After merges #1 and #3 the TOC reads:

1. Introduction
2. Setup and notation
3. Exact identity: generalized Bogoliubov sum rule
4. First consequence: isotropic trace bound
5. Second consequence: strong-locking anisotropic identity
6. Parity-mixed pairing
7. Controlled departure I: intermediate SOC
8. Controlled departure II: finite Zeeman field
9. Dynamic counterpart: spin FGT sum rule
10. Structural extension: decoupled multiband baseline
11. Core diagnostic: Knight-shift ellipsoid (opens with reference table)
12. Experimental manual: six protocols
13. Worked example: K$_2$Cr$_3$As$_3$
14. Summary

That's down from 16 top-level sections to 14, with the measurement side (11–13) cleanly proportioned to the theory side (3–10), and the reference table sitting at the natural entry point for readers who jump to the measurement material. The overall shape is now more readable without any loss of content.

---
## 🧑‍💻 User

Pls go through this revised version.

---
## 🤖 Assistant

## Review of v17

I went through the full manuscript carefully. The merges were applied cleanly, the title change is in, and the introduction rewrite reads well. There is **one serious issue** that will cause the PDF to compile incorrectly, plus a few smaller items.

## Critical: Sec. XI (Core Diagnostic) is Truncated

Between the opening sentence "For scalar hyperfine coupling…" and the start of Sec. XII ("Experimental manual"), the content of old Sec. XIII has been **accidentally deleted**. The current file goes from:

```latex
\subsection{Knight-shift tensor and ellipsoid representation}

For scalar hyperfine coupling $A^{(\mathbf{R})}_{\mu\nu}=A^{(\mathbf{R})}\delta_{\mu\nu}$ (the default setting of this subsection), the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:
	
\section[Experimental Manual]{Experimental manual: six protocols}
```

The paragraph ends mid-sentence with a colon, and everything between it and Sec. XII is missing: Eqs. `eq:Kdef`, `eq:Kscalar`, `eq:ellipsoid`, `eq:Kellipsoid`, `eq:Ki-pi`, `eq:trace-from-ellipsoid`, `eq:Khf-ellipsoid`, `eq:Khf-trace`, `eq:Khf-bound`, `eq:K-intermediate`, `eq:Pi-eff`, Fig. `fig:simplex`, Table `tab:ellipsoids`, and all surrounding text.

**Every one of those equations and the two figures/tables is referenced elsewhere in the paper.** The PDF will be littered with `??` markers and fail to convey the central ellipsoid theorem. This must be restored before submission.

### Required Restoration

Here is the content to paste between "…linearly related to the electronic spin susceptibility:" and `\section[Experimental Manual]{…}`. It reproduces the v16 content with the opening sentence already in place:

```latex
\begin{equation}
	K_{\mu\nu}(T)=A^{(\mathbf{R})}\chi_{\mu\nu}(T).
	\label{eq:Kdef}
\end{equation}
For isotropic hyperfine we define $K_{N}\equiv A\chi_{N}$; the diagonal anisotropic case is treated in Sec.~\ref{sec:ellipsoid-hf}. The dimensionless ratio $K_{\mu\nu}(T)/K_{\mu\nu}(T_{c})=\chi_{\mu\nu}(T)/\chi_{N}$ eliminates the hyperfine prefactor.

Under rotation of a single crystal in an applied field of direction $\hat{\mathbf{H}}$, NMR measures the scalar shift
\begin{equation}
	K(\hat{\mathbf{H}},T)\equiv\sum_{\mu\nu}\hat H_{\mu}K_{\mu\nu}(T)\hat H_{\nu}=\hat{\mathbf{H}}\cdot K(T)\cdot\hat{\mathbf{H}}.
	\label{eq:Kscalar}
\end{equation}
The symmetric tensor $K_{\mu\nu}(T)$ has three principal values $K_{1},K_{2},K_{3}\ge 0$ with orthonormal principal axes. The locus
\begin{equation}
	\mathcal{E}_{K}(T)\equiv\big\{\mathbf{x}\in\mathbb{R}^{3}\;:\;\mathbf{x}\cdot K(T)\cdot\mathbf{x}=1\big\}
	\label{eq:ellipsoid}
\end{equation}
is the \emph{Knight-shift ellipsoid}: semi-axes $1/\sqrt{K_{i}(T)}$.\footnote{Equation~\eqref{eq:ellipsoid} uses the non-inverted form so that degenerate limits $K_{i}\to 0$ (e.g., OSP pairing with $\mathbf{d}\parallel\hat z$ giving $K_{c}(0)=0$) are directly represented as the quadric collapsing along the corresponding axis; the standard inverted form is ill-defined at the vertices of the simplex below.} It is the NMR analogue of the susceptibility indicatrix of Nye~\cite{Nye_book}. Six independent direction measurements determine $\mathcal{E}_{K}(T)$ fully.

\subsection{The $T=0$ ellipsoid in the strong-locking regime}

Substituting the strong-locking identity Eq.~\eqref{eq:unified} into Eqs.~\eqref{eq:Kdef}--\eqref{eq:Kscalar},
\begin{equation}
	\boxed{\;K(\hat{\mathbf{H}},0)=K_{N}\left[1-\hat{\mathbf{H}}\cdot\Pi\cdot\hat{\mathbf{H}}\right],\;}
	\label{eq:Kellipsoid}
\end{equation}
with $K_{N}\equiv K(\hat{\mathbf{H}},T_{c}^{+})$. The principal-axis frame of $\mathcal{E}_{K}(0)$ coincides with that of $\Pi$, and
\begin{equation}
	\frac{K_{i}(0)}{K_{N}}=1-\pi_{i},\qquad i=1,2,3.
	\label{eq:Ki-pi}
\end{equation}
The three eigenvalues $\pi_{i}\in[0,1]$ of $\Pi$ satisfy $\pi_{1}+\pi_{2}+\pi_{3}=\mathrm{Tr}\,\Pi=1$, so the $T=0$ principal values obey
\begin{equation}
	\boxed{\;\sum_{i}K_{i}(0)=2K_{N}.\;}
	\label{eq:trace-from-ellipsoid}
\end{equation}
This simplex classification is a statement about the locking tensor, not by itself about the parity label. As Sec.~\ref{sec:paritymix} shows, a fully gapped helicity-diagonal parity-mixed state lands on the same $T=0$ ellipsoid as the corresponding pure locking texture; distinguishing parity admixture then requires finite-$T$ information or other probes.

\subsection{Allowed shapes and the pairing-class catalogue}

The constraint $\pi_{1}+\pi_{2}+\pi_{3}=1$ with $0\le\pi_{i}\le 1$ confines the allowed ellipsoids to a two-dimensional simplex (Fig.~\ref{fig:simplex}). Each vertex, edge, and interior point corresponds to a distinct pairing class or locking-vector texture. Table~\ref{tab:ellipsoids} catalogues the canonical cases.

\begin{figure}[tb]
	\centering
	\begin{tikzpicture}[scale=3.2, font=\small]
		\coordinate (V1) at (-1, 0);
		\coordinate (V2) at ( 1, 0);
		\coordinate (V3) at ( 0, 1.7320508);
		\coordinate (M12) at ( 0, 0);
		\coordinate (M13) at (-0.5, 0.8660254);
		\coordinate (M23) at ( 0.5, 0.8660254);
		\coordinate (B) at ( 0, 0.5773503);
		\fill[gray!8] (V1) -- (V2) -- (V3) -- cycle;
		\draw[thick] (V1) -- (V2) -- (V3) -- cycle;
		\draw[gray!55, dashed, thin] (V1) -- (M23);
		\draw[gray!55, dashed, thin] (V2) -- (M13);
		\draw[gray!55, dashed, thin] (V3) -- (M12);
		\fill (V1) circle (0.024);
		\fill (V2) circle (0.024);
		\fill (V3) circle (0.024);
		\fill[red!80!black] (M12) circle (0.024);
		\fill[red!80!black] (M13) circle (0.024);
		\fill[red!80!black] (M23) circle (0.024);
		\fill[blue!70!black] (B) circle (0.033);
		\node[below=3pt, font=\scriptsize] at (V1) {$(1,0,0)$};
		\node[below=3pt, font=\scriptsize] at (V2) {$(0,1,0)$};
		\node[above=3pt, font=\scriptsize] at (V3) {$(0,0,1)$};
		\node[below=4pt, font=\scriptsize] at (M12) {$(\tfrac{1}{2},\tfrac{1}{2},0)$};
		\node[left=4pt, font=\scriptsize] at (M13) {$(\tfrac{1}{2},0,\tfrac{1}{2})$};
		\node[right=4pt, font=\scriptsize] at (M23) {$(0,\tfrac{1}{2},\tfrac{1}{2})$};
		\node[right=6pt, font=\scriptsize] at (B) {$(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$};
		\draw[->, thick, blue!60!black, shorten >=1pt] ($(B)+(210:0.28)$) -- ($(B)+(210:0.02)$);
		\node[below left=1pt, font=\scriptsize, blue!60!black] at ($(B)+(210:0.28)$) {intermediate SOC};
	\end{tikzpicture}
	\caption{Simplex of allowed $T=0$ Knight-shift ellipsoids in the strong-locking regime, parametrized by the eigenvalues $(\pi_{1},\pi_{2},\pi_{3})$ of $\Pi$ with $\sum_{i}\pi_{i}=1$, $\pi_{i}\in[0,1]$ [Eq.~\eqref{eq:Kellipsoid}]. Vertices (black): oblate-axial ellipsoids from OSP triplet or quasi-1D SOC along one crystal axis. Edge midpoints (red): prolate-axial ellipsoids from ESP triplet in a plane or 2D Rashba SOC confined to that plane. Barycenter (blue): isotropic sphere from singlet with strong SOC or isotropic 3D SOC. Interior points correspond to tilted locking textures. Blue arrow: radial contraction of a strong-locking point toward the origin at intermediate SOC (for uniform $|\mathbf{g}|/\Delta$, $p_{i}=F_{s}(\lambda)\pi_{i}$; see Sec.~\ref{sec:ellipsoid}). Full classification in Table~\ref{tab:ellipsoids}.}
	\label{fig:simplex}
\end{figure}

\begin{table*}[tb]
	\caption{Canonical $T=0$ Knight-shift ellipsoid shapes and the locking-vector textures that produce them in the strong-locking regime. An \emph{oblate} axial ellipsoid is flattened along the symmetry axis (disk-like); a \emph{prolate} axial ellipsoid is elongated along the symmetry axis (rod-like).}
	\label{tab:ellipsoids}
	\renewcommand\arraystretch{1.3}
	\setlength{\tabcolsep}{0.8ex}
	\begin{tabular}{l|c|l|l}
		\hline\hline
		Pairing/texture & $(\pi_{1},\pi_{2},\pi_{3})$ & Shape & Principal-values ratio\\
		\hline
		singlet, strong SOC & $(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$ & sphere & $K_{1}=K_{2}=K_{3}=\tfrac{2}{3}K_{N}$\\
		OSP, $\mathbf{d}\parallel\hat z$ & $(0,0,1)$ & oblate axial & $K_{x,y}=K_{N}$, $K_{z}=0$\\
		ESP, $\mathbf{d}\in xy$ (axial) & $(\tfrac{1}{2},\tfrac{1}{2},0)$ & prolate axial & $K_{x,y}=\tfrac{1}{2}K_{N}$, $K_{z}=K_{N}$\\
		2D Rashba in $ab$ & $(\tfrac{1}{2},\tfrac{1}{2},0)$ & prolate axial & same as ESP axial\\
		quasi-1D along $\hat c$ & $(0,0,1)$ & oblate axial & same as OSP axial\\
		tilted Rashba & generic, $\sum=1$ & triaxial & three distinct $K_{i}$\\
		\hline\hline
	\end{tabular}
\end{table*}

Figure~\ref{fig:simplex} and Table~\ref{tab:ellipsoids} together form the classification: the simplex identifies where a measured point sits, and the table gives the corresponding pairing/texture interpretation and principal-value ratios. Four observations make the table an experimental diagnostic.

(i) \emph{Axial vs triaxial.} An axial ellipsoid ($K_{1}=K_{2}\ne K_{3}$) indicates that $\Pi$ has one distinguished eigenvalue: either $\pi=1$ on one axis (oblate: OSP or quasi-1D) or $\pi=0$ on one axis balanced by $\pi=1/2$ on the other two (prolate: ESP or 2D Rashba). A triaxial ellipsoid indicates a tilted locking texture.

(ii) \emph{Oblate vs prolate.} In the oblate case $K_{3}/K_{1,2}\to 0$ (ellipsoid collapses to a disk); in the prolate case $K_{3}/K_{1,2}\to 2$ (ellipsoid is rod-like). The direction of anisotropy identifies the $\mathbf{d}$-vector axis (OSP, oblate \emph{along} $\mathbf{d}$) or the plane of the 2D locking texture (ESP/2D Rashba, prolate \emph{perpendicular} to the plane).

(iii) \emph{Trace ratio.} Eq.~\eqref{eq:trace-from-ellipsoid} guarantees $\sum_{i}K_{i}(0)=2K_{N}$ in the strong-locking regime. Deviations signal (a) intermediate SOC, where $\sum_{i}K_{i}(0)=2K_{N}\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}\le 2K_{N}$ by Sec.~\ref{sec:intermediate}, (b) multi-band decomposition, or (c) breakdown of the single-band unitary BdG framework.

(iv) \emph{Nucleus independence.} By Sec.~\ref{sec:specializations}, different nuclei with scalar hyperfine couplings map to ellipsoids that differ by an overall scale but share the same principal axes and normalized principal values; they must map to the same point of Fig.~\ref{fig:simplex}.

\subsection{Anisotropic hyperfine coupling}
\label{sec:ellipsoid-hf}

For a diagonal hyperfine tensor $A^{(\mathbf{R})}=\mathrm{diag}(A_{1},A_{2},A_{3})$ coaxial with $\chi_{\mu\nu}$ and $\Pi_{\mu\nu}$,
\begin{equation}
	K_{i}(0)=A_{i}\chi_{N}(1-\pi_{i}),\qquad i=1,2,3,
	\label{eq:Khf-ellipsoid}
\end{equation}
so the anisotropic hyperfine rescales the semi-axes but preserves normalized principal-value ratios. The strong-locking trace identity becomes
\begin{align}
	\sum_{i}\frac{K_{i}(0)}{K_{i}(T_{c}^{+})} &= 2, \label{eq:Khf-trace}\\
	0\le\frac{K_{i}(0)}{K_{i}(T_{c}^{+})} &= 1-\pi_{i}\le 1. \label{eq:Khf-bound}
\end{align}
Non-coaxial hyperfine and susceptibility frames require an independent determination of $A$; we do not pursue that case here.

\subsection{Intermediate-SOC regime: ellipsoid contraction}

In the intermediate-SOC $s$-wave case of Eq.~\eqref{eq:chi-explicit}, the scalar-hyperfine Knight shift reads
\begin{widetext}
	\begin{equation}
		\frac{K(\hat{\mathbf{H}},0)}{K_{N}}=\big\langle F_{s}(\lambda_{\mathbf{k}})\big[1-(\hat{\mathbf{H}}\cdot\hat n_{\mathbf{k}})^{2}\big]\big\rangle_{\rm FS}
		\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
		\label{eq:K-intermediate}
	\end{equation}
\end{widetext}
with $S(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$ and
\begin{equation}
	\Pi^{\rm eff}_{\mu\nu}(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS},\qquad \mathrm{Tr}\,\Pi^{\rm eff}=S(\lambda)\le 1.
	\label{eq:Pi-eff}
\end{equation}
For uniform SOC magnitude, $\Pi^{\rm eff}=F_{s}(\lambda)\Pi$, so $p_{i}=F_{s}(\lambda)\pi_{i}$: the strong-locking ellipsoid contracts homothetically toward the origin as the SOC weakens. Fig.~\ref{fig:simplex} shows the direction of this contraction.

The output of this section is therefore a set of measurable coordinates: either the strong-locking simplex point $(\pi_{1},\pi_{2},\pi_{3})$ or, away from that limit, its contracted intermediate-SOC counterpart $(p_{1},p_{2},p_{3})$. The next section turns those coordinates into an ordered measurement program.
```

Note the one small update I made while restoring: the forward reference from "As Sec.~\ref{sec:paritymix-consequences}" has become "As Sec.~\ref{sec:paritymix}" (pointing to the merged section rather than the old subsection-only label).

## Minor Items (Non-Critical)

Once the restoration above is in place, the remaining items are cosmetic:

1. **Intro roadmap paragraph**: "Section~\ref{sec:paritymix} places parity-mixed singlet-triplet states in the same language and **show** that …" — should be "**shows**" (singular subject now that the two sections merged into one).

2. **`Plancherel1910`, `ReedSimonII`, `HornJohnson`** — confirm these three bib entries are in `mag-soc.bib`. If they are missing, add them (I listed them earlier in the review).

3. **Preamble unused packages**: `epsfig`, `multirow`, `amsbsy`, `diagbox`, `extarrows`, `txfonts`, `tablefootnote`, `\allowdisplaybreaks` — none are used in the manuscript and can be removed for a cleaner preamble. Not required, but keeps the preamble honest.

## Bottom Line

**Do not submit v17 as is.** The missing chunk in Sec. XI (the entire ellipsoid construction) will render the paper unreadable. Paste the block above into the gap, apply the one-word fix in the intro ("show" → "shows"), and you're done.

Let me know after you rebuild with the restored content — happy to do one final read-through of v18 before submission.

---
## 🧑‍💻 User

Give me the clean Preamble 

---
## 🤖 Assistant

## Clean Preamble

Here is a minimal preamble that keeps only what the manuscript actually uses:

```latex
\documentclass[prb,aps,twocolumn,superscriptaddress]{revtex4-2}

\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{bm}
\usepackage{graphicx}
\usepackage{tikz}
\usetikzlibrary{calc}

\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,bookmarks=false]{hyperref}

\graphicspath{{figures/}}
```

## What Each Line Does

- `revtex4-2` with the PRB/APS/twocolumn options — the document class.
- `amsmath` — `\begin{align}`, `\begin{equation}`, `\tfrac`, etc.
- `amssymb` — `\le`, `\ge`, `\mathbb{I}`, and other symbols.
- `bm` — `\mathbf` in equations (technically `amsmath` covers most of this, but `bm` guarantees consistent bold math).
- `graphicx` — the `\includegraphics` in Appendix A.
- `tikz` with the `calc` library — the simplex figure and the spin-FGT schematic. The `calc` library is needed for the `($(B)+(210:0.28)$)` coordinate arithmetic.
- `hyperref` — clickable cross-references and citations. Loaded last per convention.
- `\graphicspath{{figures/}}` — tells `graphicx` where to find the validation figure.

## What Was Removed and Why

| Package | Used anywhere? | Verdict |
|---------|----------------|---------|
| `color` | No (colors come from `tikz` / `hyperref`) | Remove |
| `epsfig` | No | Remove (obsolete; use `graphicx`) |
| `multirow` | No | Remove |
| `amsbsy` | No (subsumed by `bm`) | Remove |
| `array` | No custom column types | Remove |
| `diagbox` | No | Remove |
| `extarrows` | No | Remove |
| `appendix` | No (using plain `\appendix`) | Remove |
| `txfonts` | Changes font — probably unintended | Remove |
| `tablefootnote` | No | Remove |
| `\allowdisplaybreaks[4]` | No multi-page equations in the paper | Remove |
| `\newcommand{\tabincell}{…}` | Unused | Remove |

All these were baggage from an older template and none are referenced in the body.

## One Safety Check

Before committing, do a quick test compile. If anything fails, it is almost certainly one of these three:

1. **`\bm`** — if your TeX distribution doesn't ship `bm`, replace `\usepackage{bm}` with `\usepackage{amsbsy}`. Unlikely to be needed on a modern TeX Live.

2. **Font appearance changes** — if the paper looks visibly different, it's the removed `txfonts`. That package was swapping in Times-like math fonts, which is non-standard for PRB. Removing it should give you the REVTeX default, which is what PRB expects anyway.

3. **TikZ** — if a library beyond `calc` is silently needed (positioning, arrows), the error will name it. The manuscript as written uses only `calc`, so this should not trigger.

Everything else (tables, appendices, math, references) uses standard REVTeX/amsmath features with no extra packages.

---
## 🧑‍💻 User

This is the revised version.

---
## 🤖 Assistant

## Review of v17 (after Sec. XI restoration)

I've gone through the full file. The missing ellipsoid content is now in place and all the prior merges and notation fixes have landed correctly. Below is a short punch-list of what I found — **nothing is a blocker**, but a few items are worth addressing before submission.

## Items Worth Fixing

### 1. Stale roadmap phrasing in the introduction

Paragraph 4 of Sec. I:

> "Section~\ref{sec:paritymix} places parity-mixed singlet-triplet states in the same language and shows that, in the fully gapped helicity-diagonal limit, the $T=0$ projector geometry survives while the admixture is pushed primarily into the finite-$T$ recovery."

Good. But two sentences earlier in the same paragraph, at the bottom of the page:

> "Sections~\ref{sec:intermediate} and~\ref{sec:finiteH} then relax one assumption at a time…"

This is fine. Then near the end of Sec. IV ("Second consequence"):

> "The next **two sections** show that the fully gapped helicity-diagonal limit preserves the $T=0$ projector geometry, and that parity admixture primarily reorganizes the finite-$T$ recovery."

Since V and VI were merged into one section, "two sections" is now wrong. Change to:

> "The next **section** shows that the fully gapped helicity-diagonal limit preserves the $T=0$ projector geometry, and that parity admixture primarily reorganizes the finite-$T$ recovery."

### 2. Extra blank line between a sentence and its equation

In Sec. XI.A (Knight-shift tensor and ellipsoid representation):

```latex
the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:

\begin{equation}
    K_{\mu\nu}(T)=A^{(\mathbf{R})}\chi_{\mu\nu}(T).
```

The blank line between the colon and `\begin{equation}` forces LaTeX to start a new paragraph, indenting the equation. Remove the blank line to get the standard "trailing colon → equation" layout:

```latex
the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:
\begin{equation}
    K_{\mu\nu}(T)=A^{(\mathbf{R})}\chi_{\mu\nu}(T).
```

Cosmetic, but noticeable in the typeset output.

### 3. Unused `hyperref` option for `bookmarks=false`

Minor: `bookmarks=false` disables PDF bookmarks for the TOC, which is fine if intentional, but most readers appreciate a bookmarked TOC. If you want bookmarks back, remove `bookmarks=false`. Not a bug.

### 4. Forward reference in the strong-locking Eq. (21) error discussion

Sec. VI, Eq. `eq:paritymix-chiT` caption comment:

> "The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction originates from the strong-SOC expansion of the inter-helicity denominator, exactly as in Eq.~\eqref{eq:strongH-identity}."

`eq:strongH-identity` is in Sec. VIII, which comes *after* Sec. VI. This forward reference is correct but slightly confusing. A reader-friendlier phrasing:

> "The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction has the same three sources catalogued below Eq.~\eqref{eq:strongH-identity}."

Or, if you want to avoid the forward reference entirely:

> "The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction originates from the strong-SOC expansion of the inter-helicity denominator; its structure mirrors the finite-field case in Sec.~\ref{sec:finiteH}."

Either is fine. Not a must-fix.

### 5. Citation checks

Spot-check these three new bib entries exist in `mag-soc.bib`:
- `Plancherel1910`
- `ReedSimonII`
- `HornJohnson`

They were added in the Plancherel-reference round. If any are still missing, you'll get `[?]` in the PDF.

## Items That Are Fine (Confirmed)

- Title updated: **"Plancherel sum rules and Knight-shift geometry in noncentrosymmetric superconductors"** ✓
- Preamble is clean ✓
- Intro rewrites (historical narrative, companion-paper mention, Plancherel definition + references) all present ✓
- Sec. IV.B wording cleaned (no redundant $|\mathbf{d}|$ condition) ✓
- Sec. V+VI merge complete; cross-references `sec:paritymix-structure` and `sec:paritymix-consequences` still valid as subsection labels ✓
- Sec. XII reference table now inside Sec. XI as subsection A, with `tab:keyresults` label intact ✓
- Sec. XI (Core diagnostic) fully restored: all equations (eq:Kdef, eq:Kscalar, eq:ellipsoid, eq:Kellipsoid, eq:Ki-pi, eq:trace-from-ellipsoid, eq:Khf-*, eq:K-intermediate, eq:Pi-eff), Fig. `fig:simplex`, Table `tab:ellipsoids` are all in place ✓
- $\Pi_{\mu\mu}$ / $\Pi_{\alpha\alpha}$ conventions consistent in Sec. VIII, Table IV, and Figs. ✓
- K₂Cr₃As₃ section uses the parenthetical $\pi_a \equiv \Pi_{aa}$ identification ✓
- Protocol D step 3 points at `eq:T1-diagnostic` correctly ✓
- TOC structure: 14 top-level sections + 2 appendices, cleanly proportioned ✓

## Bottom Line

The manuscript is in submission shape. Items 1 and 2 above are tiny wording/layout fixes I'd recommend before final sign-off. Items 3–5 are optional or just verification steps.

Once you make those tweaks, do one clean compile (bibtex pass included) and scan the PDF for any residual `??` markers. If everything resolves, you're ready to submit.

It has been a pleasure working through this with you. The paper reads as a coherent, well-organized piece now, with a clear logical spine from the Plancherel identity to the K$_2$Cr$_3$As$_3$ diagnosis. Good luck with the submission.

---
## 🧑‍💻 User

4. Forward reference in the strong-locking Eq. (21) error discussion: could you give me the whole paragraph?

---
## 🤖 Assistant

## Sec. VI Paragraph with Forward Reference Softened

Here is the full paragraph immediately following Eq. `eq:paritymix-chiT`. The final sentence is rewritten to remove the direct forward reference to Sec. VIII's Eq. `eq:strongH-identity`.

```latex
\begin{equation}
	\frac{\chi_{\mu\nu}(T)}{\chi_{N}}
	=
	\delta_{\mu\nu}-\Pi_{\mu\nu}
	+
	\sum_{\lambda=\pm}w_{\lambda}
	\left\langle
	Y_{\lambda}(\mathbf{k},T)\hat g_{\mu}(\mathbf{k})\hat g_{\nu}(\mathbf{k})
	\right\rangle_{\lambda}
	+O(\Delta^{2}/|\mathbf{g}|^{2}),
	\label{eq:paritymix-chiT}
\end{equation}
with $\langle\cdots\rangle_{\lambda}$ the FS average over the $\lambda$-helicity sheet, $w_{\lambda}=N_{\lambda}(0)/N(0)$, and
\begin{equation}
	Y_{\lambda}(\mathbf{k},T)=-\!\int\!d\xi\,\frac{\partial f}{\partial E}\bigg|_{E_{\lambda}(\mathbf{k})}
\end{equation}
the standard Yosida function built from $|\Delta_{\lambda}(\mathbf{k})|$, and $\Pi_{\mu\nu}\equiv\sum_{\lambda}w_{\lambda}\langle\hat g_{\mu}\hat g_{\nu}\rangle_{\lambda}$ is the helicity-resolved form of Eq.~\eqref{eq:Pidef}. The dropped $O(\Delta^{2}/|\mathbf{g}|^{2})$ correction originates from the strong-SOC expansion of the inter-helicity denominator; the same three sources of correction---denominator expansion, $\Delta_{\perp}$-mediated sector mixing, and coherence-factor corrections---are catalogued in the finite-field analysis of Sec.~\ref{sec:finiteH}.
```

The rewrite:

- **Removes** the direct pointer to `Eq.~\eqref{eq:strongH-identity}` (which sits in a later section).
- **Names the three sources in place** so Sec. VI is now self-contained on the origin of the error.
- **Points the reader to Sec. VIII** at the section level, where the detailed catalogue lives, so anyone who wants the formal tabulation can find it without a forward equation reference.

This keeps the logical chain clean: Sec. VI states the error, names its three sources, and notes that Sec. VIII provides the detailed finite-field treatment. No circular or awkward forward-pointing.
