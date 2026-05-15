# Sum-Rule-Spin-Susceptibility#2

## 🧑‍💻 User

This is a latex note. I would like to write up a PRB paper composed of two parts: (1) An elegant theoretical part on sum rule and inequality; (2) Useful manual for experiment.  

---
## 🤖 Assistant

Looking at your v7, the physics is all there but Part I (elegant theory) and Part II (experimental manual) are interleaved. Before I rewrite, let me lay out the structural plan so we agree on the cuts. The main reorganization principles:

1. **Pull all `experimental protocol` subsections out of the theory sections** and collect them as a dedicated protocols chapter in Part II.
2. **Move the ellipsoid+simplex diagnostic entirely into Part II** — it's the centerpiece of the manual, not a theorem.
3. **Keep all derivations, identities, and bounds in Part I**, including the worked examples that make the identities concrete (those belong to theory, not practice).
4. **Defer the K₂Cr₃As₃ analysis to Part II** as the closing worked example.

Here is the proposed structure:

```
Title, Abstract (slightly rewritten to reflect two-part structure)

\part{Theoretical framework: sum rules and geometric bounds}

 I.   Introduction
 II.  Setup and notation

 III. Generalized Bogoliubov sum rule
      A. Nambu embedding of a single-particle observable
      B. The generalized sum rule (Plancherel identity)
      C. Specializations: spin / charge / multi-orbital / hyperfine
      D. Universal T=0 bound: χ_O(0) ≤ (2/3) χ_O^N

 IV.  Trace inequality on an isotropic Fermi surface
      A. Derivation
      B. Saturation pattern (Table: limiting cases)

 V.   Anisotropic identity: the spin-locking projector
      A. Normal-state benchmark at T_c
      B. Strong-locking identity at T=0
      C. Unified formulation (SOC ↔ unitary triplet)
      D. Worked examples (2D Rashba, quasi-1D, tilted)

 VI.  Closed-form interpolation F_s(λ) at arbitrary SOC
      A. Reduction to a single integral
      B. Closed-form evaluation
      C. Properties and SOC spectroscopy
      D. Numerical cross-check against Ref.[pang2026]
      E. Heuristic triplet extension

 VII. Strong-locking identity at finite Zeeman field
      A. Structure of the finite-field problem
      B. Strong-locking identity at finite H
      C. Parity argument: O(h²/λ²) stability of the zero-field ellipsoid
      D. Worked limits; regime diagram; breakdown at H*

VIII. Spin analogue of the Ferrell–Glover–Tinkham sum rule
      A. Spectral sum rule
      B. Origin in the generalized sum rule
      C. Physical content: spectral-weight transfer
      D. Relation (not equality) to 1/T_1

 IX.  Multi-band extension
      A. Disjoint-pocket form
      B. Inter-band mixing: scope and caveats


\part{Experimental manual}

 X.   The Knight-shift ellipsoid and the simplex of pairing classes
      A. Knight-shift tensor and ellipsoid representation
      B. The T=0 simplex (Figure + Table: pairing-class catalogue)
      C. Axial vs triaxial, oblate vs prolate: reading the ellipsoid
      D. Anisotropic hyperfine coupling
      E. Intermediate-SOC: homothetic contraction

 XI.  Protocols
      A. Protocol A — trace bound from three-axis Knight shift
      B. Protocol B — full ellipsoid rotation (pairing-class diagnostic)
      C. Protocol C — finite-field rotation and SOC-texture spectroscopy
      D. Protocol D — 1/T_1 cross-check (spin-FGT budget)
      E. Protocol E — site-resolved consistency across NMR nuclei
      F. Protocol F — multi-band / pocket decomposition for A_2Cr_3As_3
      G. Summary table: what each protocol measures and its assumptions

 XII. Worked example: K_2Cr_3As_3
      A. Knight-shift inputs
      B. Direct diagnostic on the simplex
      C. Tension with the band-resolved SOC-texture prediction
      D. Site-resolved check: As1 vs As2
      E. 1/T_1 cross-check: fingerprint of finite-q FM fluctuations
      F. Verdict
      G. Caveat: inter-band pairing

XIII. Summary and outlook
```

Specific moves from v7:

- v7 §3.3 (Specializations) + §3.4 (Universal 2/3 bound) → Part I §III.C + §III.D (unchanged content)
- v7 §4.3 (protocol) → Part II §XI.A
- v7 §5 (anisotropic identity) stays in Part I §V, **but** its experimental protocol → §XI.B
- v7 §6 (Knight-shift ellipsoid) → Part II §X in full, including Fig. simplex and Table ellipsoids
- v7 §6.6 (protocol) → Part II §XI.B
- v7 §7 (multiband A₂Cr₃As₃ predictions) → split: structural prediction Eqs. stay in Part I §IX; the A₂Cr₃As₃-specific parametrization plus pocket-decomposition protocol → Part II §XI.F
- v7 §8 (intermediate-SOC) → Part I §VI (unchanged)
- v7 §9 (finite-H) stays in Part I §VII; its protocol → Part II §XI.C
- v7 §10 (spin-FGT) stays in Part I §VIII; its protocol → Part II §XI.D
- v7 §11 (K₂Cr₃As₃) → Part II §XII

Two small additions I'd suggest:

- A **Part-II opening paragraph** that tells the experimentalist: "all you need is a three-axis (or full-rotation) Knight shift plus orientation-resolved 1/T₁; here is the decision tree." Followed by a flowchart or decision table.
- A **summary protocol table** in §XI.G with columns: protocol / measurement / output / assumptions / failure mode. This is what makes it a manual rather than an essay.

Two questions before I do the full rewrite:

1. Do you want `\part{}` dividers (they render as "Part I", "Part II" centered on their own page in revtex4-2), or would you prefer a lighter two-chapter feel using just section-level titles like `\section*{Part I: …}`?
2. Do you want the K₂Cr₃As₃ material kept verbatim in Part II, or should it be trimmed (the v7 version is quite long and has some repetition between §11.3 and §11.6)?

Once you confirm, I'll produce `SumRule-v8.tex` in full.

---
## 🧑‍💻 User

Not real \part{}, just in logic. K2Cr3As3 should be trimmed.

---
## 🤖 Assistant

Got it. Let me restructure into a logical two-part paper (theory then manual) using section ordering and a short bridge, and trim the K₂Cr₃As₃ section. I'll write `SumRule-v8.tex`.
</br>

Before I write, let me verify I'm working in the right directory and confirm the existing file.

```bash
ls
```

Let me first check the directory contents.

---
## 🧑‍💻 User

Just give me latex codes section by section in blocks here.

---
## 🤖 Assistant

I'll give you the v8 in section-by-section blocks. The two-part structure uses section titles and a bridge paragraph rather than real `\part{}`. All experimental protocols are pulled out of theory sections and consolidated in §XI; the ellipsoid/simplex moves entirely to Part II; K₂Cr₃As₃ is trimmed.

## Preamble, title, abstract

```latex
\documentclass[prb,aps,onecolumn,superscriptaddress]{revtex4-2}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{amsmath}
\usepackage{subfigure}
\usepackage{color}
\usepackage{bm}
\usepackage{amssymb}
\usepackage{epsfig}
\usepackage{multirow}
\usepackage{amsbsy}
\usepackage{array}
\usepackage{diagbox}
\usepackage{bm}
\usepackage{extarrows}
\usepackage{graphicx}
\usepackage{appendix}
\usepackage{txfonts}
\usepackage{lipsum}
\usepackage{tablefootnote}
\usepackage{cancel}
\usepackage{soul}
\graphicspath{{figures/}}
\allowdisplaybreaks[4]
\newcommand{\tabincell}[2]{\begin{tabular}{@{}#1@{}}#2\end{tabular}}

\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,bookmarks=false]{hyperref}

\begin{document}

\title{Sum rules, geometric bounds, and an experimental manual for the NMR response of noncentrosymmetric superconductors}

\author{Yi Zhou}
\email{yizhou@iphy.ac.cn}
\affiliation{Institute of Physics, Chinese Academy of Sciences, Beijing 100190, China}

\date{\today}

\begin{abstract}
We present a unified sum-rule framework for the NMR response of single-band noncentrosymmetric superconductors in arbitrary Zeeman field and Rashba-type spin-orbit coupling (SOC), organized in two parts. \emph{Part~I} (theory) establishes the framework. A Plancherel identity $\sum|M_{ph,O}|^{2}+\sum|M_{pp,O}|^{2}=\mathrm{Tr}_{s}(O^{2})$, valid for every Hermitian single-particle operator $O$, underlies (i) a trace bound $\mathrm{Tr}\,\chi(0)\le\tfrac{2}{3}\mathrm{Tr}\,\chi(T_{c})=2\chi_{N}$ on a 3D isotropic Fermi surface; (ii) a strong-locking anisotropic identity $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ with the locking projector $\Pi_{\mu\nu}=\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$; (iii) a closed-form $s$-wave interpolation $F_{s}(\lambda)=1-\sinh^{-1}\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ at arbitrary SOC, validated against existing numerics to $10^{-3}$; (iv) a finite-field extension $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]$ stable to $O(h^{2}/\lambda^{2})$ against small applied fields; (v) a spin analogue of the Ferrell--Glover--Tinkham sum rule tying the Knight-shift deficit to integrated pair-breaking spectral weight; and (vi) the multi-band decomposition. \emph{Part~II} (manual) converts these identities into experimental practice: the Knight-shift ellipsoid theorem and the two-dimensional simplex of pairing classes (one-to-one map from ellipsoid geometry to locking texture); a hyperfine-invariant site-resolved bound as an internal consistency check; and six protocols covering trace-bound tests, full-ellipsoid diagnostics, finite-field SOC-texture spectroscopy, $1/T_{1}$ cross-checks, site-resolved tests, and pocket decomposition. Applied to the $^{75}$As NMR data on K$_{2}$Cr$_{3}$As$_{3}$, the framework places the observed projection at the oblate-axial vertex $(0,0,1)$, saturates the trace bound, selects a rigid common $\mathbf{d}\parallel\hat c$ on all three bands over the independent-pocket SOC-texture baseline, and identifies the suppression of $1/T_{1}\parallel\hat c$ as a fingerprint of finite-$\mathbf{q}$ ferromagnetic spin-fluctuation gap formation. Regimes outside strong locking, most notably Bogoliubov-Fermi-surface formation, are explicitly outside the closed-form reach of the framework.
\end{abstract}

\maketitle

\tableofcontents
```

## §1 Introduction

```latex
\section{Introduction}
\label{sec:intro}

Reference~\cite{pang2026} developed a self-consistent single-band Bogoliubov--de Gennes (BdG) theory for the static uniform spin susceptibility $\chi_{\mu\nu}(T)$ of a superconductor under simultaneous Zeeman field and Rashba-type spin-orbit coupling (SOC)~\cite{Rashiba1960,Dresselhaus}. A key technical ingredient there is a matrix-element sum rule (Eq.~(14) of Ref.~\cite{pang2026}) on the Bogoliubov transformation. In this paper we show that this sum rule is one member of a broader family and work out its physical consequences for NMR observables: Knight shift, its angular dependence, its response to applied field, and its dynamical partner $1/T_{1}$.

The paper is organized in two parts. \emph{Part~I} (Secs.~\ref{sec:setup}--\ref{sec:multiband}) develops the theory. Section~\ref{sec:setup} fixes notation. Section~\ref{sec:generalized} establishes the generalized sum rule as a Plancherel identity; the spin-sector version of Ref.~\cite{pang2026} is one specialization, and charge, multi-orbital, and site-resolved variants follow. Sections~\ref{sec:isoT0}--\ref{sec:anisoT0} specialize to the $T=0$ static spin susceptibility, yielding the trace bound and the anisotropic identity in the strong-locking regime. Section~\ref{sec:intermediate} presents the closed-form $F_{s}(\lambda)$ interpolation for $s$-wave pairing at arbitrary SOC. Section~\ref{sec:finiteH} extends the anisotropic identity to finite Zeeman field; a parity argument establishes quadratic stability of the zero-field result. Section~\ref{sec:spinFGT} derives the spin analogue of the Ferrell--Glover--Tinkham sum rule. Section~\ref{sec:multiband} gives the multi-band decomposition.

\emph{Part~II} (Secs.~\ref{sec:ellipsoid}--\ref{sec:K2Cr3As3}) is an experimental manual. Section~\ref{sec:ellipsoid} states the Knight-shift ellipsoid theorem: rotating the applied field on a single crystal at $T=0$ produces a quadric surface whose principal values, together with the trace constraint of Part~I, diagnose the pairing class via a two-dimensional simplex. Section~\ref{sec:protocols} collects six self-contained measurement protocols covering trace-bound tests, ellipsoid diagnostics, finite-field SOC-texture spectroscopy, $1/T_{1}$ cross-checks, site-resolved consistency, and pocket decomposition. Section~\ref{sec:K2Cr3As3} applies the manual to K$_{2}$Cr$_{3}$As$_{3}$ using the $^{75}$As data of Yang \emph{et al.}~\cite{Triplet2021}. Section~\ref{sec:summary} summarizes.

The broader context of noncentrosymmetric superconductors and their Knight-shift phenomenology~\cite{Reif1957,AndroesKnight1959,Ferrell1959,Kadanoff1959,Schrieffer1959,AndersonKnight1959,Andersontheoryofdirty1959,Appel1965,shiba1976effect,zhogolev1972magnetic,Frigeri2004,Frigeri_2004,Samokhin2007,Edelstein2008,bauer2012non,Yip14,Samohkin15,Smidman17} frames the discussion.
```

## §2 Setup and notation

```latex
\section{Setup and notation}
\label{sec:setup}

We adopt the single-band BdG framework of Refs.~\cite{pang2025,pang2026,BCS1957,deGennes,tinkham}. The mean-field Hamiltonian $H=H_{0}+H_{\rm SC}$ has a normal-state part
\begin{equation}
	H_{0}(\mathbf{k})=\xi_{\mathbf{k}}\sigma_{0}+\mu_{B}\mathbf{H}\cdot\hat\sigma+\mathbf{g}_{\mathbf{k}}\cdot\hat\sigma,
	\label{eq:H0gen}
\end{equation}
with $\mathbf{g}_{\mathbf{k}}$ a general SOC vector (not necessarily $g\mathbf{k}$), and pairing matrix $\Delta(\mathbf{k})=i[\Delta\sigma_{0}+\mathbf{d}(\mathbf{k})\cdot\hat\sigma]\sigma_{y}$~\cite{Balian1963,Sigrist1991,Leggett1975}. Diagonalization by
\begin{equation}
	c_{\mathbf{k}\alpha}=\sum_{s=\pm}\!\left(u^{\alpha s}_{\mathbf{k}}\psi_{\mathbf{k}s}+v^{\alpha s}_{\mathbf{k}}\psi^{\dagger}_{-\mathbf{k}s}\right)
	\label{eq:BdGtrans}
\end{equation}
decomposes the static uniform spin susceptibility as $\chi_{\mu\mu}=\chi^{ph+}_{\mu\mu}+\chi^{ph-}_{\mu\mu}+\chi^{pp+}_{\mu\mu}+\chi^{pp-}_{\mu\mu}$, with each term non-negative~\cite{pang2026}.

The Nambu spinor $C_{\mathbf{k}}=(c_{\mathbf{k}\uparrow},c_{\mathbf{k}\downarrow},c^{\dagger}_{-\mathbf{k}\uparrow},c^{\dagger}_{-\mathbf{k}\downarrow})^{T}$ relates to the quasiparticle basis $\Psi_{\mathbf{k}}=(\psi_{\mathbf{k}+},\psi_{\mathbf{k}-},\psi^{\dagger}_{-\mathbf{k}+},\psi^{\dagger}_{-\mathbf{k}-})^{T}$ by $C_{\mathbf{k}}=U_{\mathbf{k}}\Psi_{\mathbf{k}}$ with
\begin{equation}
	U_{\mathbf{k}}=\begin{pmatrix}u_{\mathbf{k}} & v_{\mathbf{k}}\\v^{*}_{-\mathbf{k}} & u^{*}_{-\mathbf{k}}\end{pmatrix},\qquad U^{\dagger}_{\mathbf{k}}U_{\mathbf{k}}=\mathbb{I}_{\rm BdG}.
	\label{eq:Umatrix}
\end{equation}
$\mathrm{Tr}_{s}$ denotes a trace over the single-particle spin (or spin$\otimes$orbital) space and $\mathrm{Tr}_{\rm BdG}$ the doubled Nambu trace.

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
is symmetric, positive semi-definite, with $\mathrm{Tr}\,\Pi=1$. This tensor is the geometric object that organizes both parts of the paper.
```

Let me know if the tone and structure look right so far; then I'll continue with §3 (generalized sum rule) and onward.

---
## 🧑‍💻 User

Sounds good. go ahead

---
## 🤖 Assistant

## §3 Generalized Bogoliubov sum rule

```latex
\section{Generalized Bogoliubov matrix-element sum rule}
\label{sec:generalized}

We present the sum rule of Ref.~\cite{pang2026} as one specialization of a Plancherel-type identity on the Bogoliubov transformation. This framing makes the geometric content manifest and generates on demand the charge, multi-orbital, and site-resolved variants used later.

\subsection{Nambu embedding of a single-particle observable}

Let $O$ be any Hermitian operator on the single-particle space. Its bilinear $\hat{O}_{\mathbf{k}}=\sum_{\alpha\beta}c^{\dagger}_{\mathbf{k}\alpha}O_{\alpha\beta}c_{\mathbf{k}\beta}$ can be rewritten in Nambu form as
\begin{equation}
	\hat{O}_{\mathbf{k}}=C^{\dagger}_{\mathbf{k}}\,\mathcal{O}_{\rm BdG}\,C_{\mathbf{k}}+\tfrac{1}{2}\mathrm{Tr}_{s}(O),\quad \mathcal{O}_{\rm BdG}=\tfrac{1}{2}\begin{pmatrix}O & 0\\0 & -O^{T}\end{pmatrix}.
	\label{eq:Oembedding}
\end{equation}
The Nambu ordering follows Eq.~\eqref{eq:Umatrix}. The minus sign in $-O^{T}$ is forced by the doubling structure and, together with Hermiticity of $O$, makes $\mathcal{O}_{\rm BdG}$ Hermitian. The constant is absorbed into the chemical potential. Using $O^{T}=O^{*}$ for Hermitian $O$,
\begin{equation}
	\mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG})=0,\qquad \mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG}^{2})=\tfrac{1}{2}\mathrm{Tr}_{s}(O^{2}).
	\label{eq:BdGtrace}
\end{equation}

\subsection{The generalized sum rule}

Transforming to the quasiparticle basis, $\tilde{\mathcal{O}}_{\mathbf{k}}=U^{\dagger}_{\mathbf{k}}\mathcal{O}_{\rm BdG}U_{\mathbf{k}}$, yields the block form
\begin{equation}
	\tilde{\mathcal{O}}_{\mathbf{k}}=\tfrac{1}{2}\!\begin{pmatrix}M_{ph,O}(\mathbf{k}) & M_{pp,O}(\mathbf{k}) \\ M_{pp,O}^{\dagger}(\mathbf{k}) & \widetilde{M}_{ph,O}(\mathbf{k})\end{pmatrix},
	\label{eq:block}
\end{equation}
with
\begin{align}
	M_{ph,O}(\mathbf{k}) & =u^{\dagger}_{\mathbf{k}}Ou_{\mathbf{k}}-[v^{\dagger}_{-\mathbf{k}}Ov_{-\mathbf{k}}]^{T},\label{eq:Mph-O}\\
	M_{pp,O}(\mathbf{k}) & =u^{\dagger}_{\mathbf{k}}Ov_{\mathbf{k}}-[u^{\dagger}_{-\mathbf{k}}Ov_{-\mathbf{k}}]^{T},\label{eq:Mpp-O}
\end{align}
and $\widetilde{M}_{ph,O}(\mathbf{k})=-M_{ph,O}(-\mathbf{k})^{T}$. Unitarity of $U_{\mathbf{k}}$ and cyclicity of the trace give
\begin{equation}
	\mathrm{Tr}_{\rm BdG}(\tilde{\mathcal{O}}_{\mathbf{k}}^{2})=\mathrm{Tr}_{\rm BdG}(\mathcal{O}_{\rm BdG}^{2})=\tfrac{1}{2}\mathrm{Tr}_{s}(O^{2}).
	\label{eq:invariance}
\end{equation}
Expanding the left-hand side and symmetrizing in $\mathbf{k}\leftrightarrow-\mathbf{k}$ produces the generalized sum rule
\begin{equation}
	\boxed{\;\sum_{s_{1}s_{2}}\!\Big[\big|M^{s_{1}s_{2}}_{ph,O}(\mathbf{k})\big|^{2}+\big|M^{s_{1}s_{2}}_{pp,O}(\mathbf{k})\big|^{2}\Big]=\mathrm{Tr}_{s}(O^{2}),\;}
	\label{eq:general-sum-rule}
\end{equation}
valid at every $\mathbf{k}$ and for every Hermitian single-particle operator $O$.

\emph{Origin.} Equation~\eqref{eq:general-sum-rule} is a Plancherel identity: the Frobenius norm of a Hermitian operator is preserved by the unitary BdG transformation. In the single-particle language this is the familiar $\mathrm{Tr}[(U^{\dagger}OU)^{2}]=\mathrm{Tr}(O^{2})$; the BdG doubling adds the particle-particle sector on the left-hand side.

\emph{Relation to Ref.~\cite{pang2026}.} The sum rule Eq.~(14) of Ref.~\cite{pang2026} is the specialization $O=\sigma_{\mu}$ of Eq.~\eqref{eq:general-sum-rule} and is the only case derived there. The extension to arbitrary Hermitian $O$ enables the charge, multi-orbital, and site-resolved variants below---in particular, the hyperfine-coupled operator $O_{\rm hf}=A^{(\mathbf{R})}_{\alpha\mu}\sigma_{\mu}$ and its site-resolved bound Eq.~\eqref{eq:site-bound}.

\subsection{Specializations}
\label{sec:specializations}

\emph{(a) Spin sector.} For $O=\sigma_{\mu}$, $\mathrm{Tr}_{s}(\sigma_{\mu}^{2})=2$, reproducing Eq.~(14) of Ref.~\cite{pang2026}. Summing over $\mu=x,y,z$,
\begin{equation}
	\sum_{\mu}\sum_{s_{1}s_{2}}\big[|M_{ph,\mu}|^{2}+|M_{pp,\mu}|^{2}\big]=6.
	\label{eq:spin-total}
\end{equation}

\emph{(b) Charge sector.} For $O=\sigma_{0}$, $\mathrm{Tr}_{s}(\sigma_{0}^{2})=2$; this constrains finite-$\mathbf{q}$ charge response.

\emph{(c) Multi-orbital extension.} With orbitals, $O=\sigma_{\mu}\otimes\Lambda$ gives $\mathrm{Tr}_{s}(O^{2})=2\,\mathrm{Tr}(\Lambda^{2})$; for orbital-diagonal ($\Lambda=\mathbb{I}_{\rm orb}$) this reproduces the additive multi-pocket form of Sec.~\ref{sec:multiband}.

\emph{(d) Site-resolved hyperfine coupling.} An NMR nucleus at site $\mathbf{R}$ couples through $O_{\rm hf}=A^{(\mathbf{R})}_{\alpha\mu}\sigma_{\mu}$, giving $\mathrm{Tr}_{s}(O_{\rm hf}^{2})=2\|A^{(\mathbf{R})}\|_{F}^{2}$. After normalization by the normal-state value, the bound
\begin{equation}
	\frac{\mathrm{Tr}\,K^{(\mathbf{R})}(0)}{\mathrm{Tr}\,K^{(\mathbf{R})}(T_{c})}\le\tfrac{2}{3}
	\label{eq:site-bound}
\end{equation}
is independent of $\|A^{(\mathbf{R})}\|_{F}$. Different nuclei in a single compound therefore obey identical normalized bounds---an internal consistency check deployed as a protocol in Sec.~\ref{sec:protocols}.

\begin{table}[b]
	\caption{Hermitian operators, sum-rule weights from Eq.~\eqref{eq:general-sum-rule}, and their NMR relevance.}
	\label{tab:operators}
	\renewcommand\arraystretch{1.3}
	\setlength{\tabcolsep}{1.0ex}
	\begin{tabular}{l|l|c|l}
		\hline\hline
		Operator $O$ & Observable & $\mathrm{Tr}_{s}(O^{2})$ & NMR relevance\\
		\hline
		$\sigma_{\mu}$ & spin component & $2$ & Knight-shift component\\
		$\sum_{\mu}\sigma_{\mu}^{2}=3\mathbb{I}$ & total spin & $6$ & Knight-shift trace bound\\
		$A^{(\mathbf{R})}_{\alpha\mu}\sigma_{\mu}$ & site-$\mathbf{R}$ coupling & $2\|A^{(\mathbf{R})}\|_{F}^{2}$ & site-resolved bound\\
		$\sigma_{\mu}\otimes\mathbb{I}_{\rm orb}$ & multi-band spin & $2N_{\rm orb}$ & multi-pocket bound\\
		$\sigma_{\mu}\otimes\Lambda$ & orbital-resolved spin & $2\,\mathrm{Tr}(\Lambda^{2})$ & orbital projection\\
		\hline\hline
	\end{tabular}
\end{table}

\subsection{Universal $T=0$ consequence}

At $T=0$ only the pp channel contributes to any susceptibility~\cite{pang2026}:
\begin{equation}
	\chi_{O}(0)=\sum_{\mathbf{k}}\sum_{s_{1}s_{2}}\frac{|M_{pp,O}^{s_{1}s_{2}}(\mathbf{k})|^{2}}{E_{\mathbf{k}s_{1}}+E_{-\mathbf{k}s_{2}}}.
	\label{eq:chiO-T0}
\end{equation}
Equation~\eqref{eq:general-sum-rule} bounds the numerator pointwise: $\sum_{s_{1}s_{2}}|M_{pp,O}|^{2}\le\mathrm{Tr}_{s}(O^{2})$ per $\mathbf{k}$. Combined with the FS geometric factor $\langle\cos^{2}\theta\rangle_{\rm FS}=1/3$ (Eq.~(17) of Ref.~\cite{pang2026}) on a 3D isotropic FS, this gives the operator-independent bound
\begin{equation}
	\boxed{\;\chi_{O}(0)\le\tfrac{2}{3}\,\chi_{O}^{N},\;}
	\label{eq:universal-23}
\end{equation}
with the same $2/3$ factor regardless of which Hermitian operator $O$ is probed. The $2/3$ is a geometric property of the 3D spin-locking direction, not special to the spin sector. Equation~\eqref{eq:general-sum-rule} is the single organizing principle from which all results of this paper follow as specializations.
```

## §4 Trace sum rule on an isotropic Fermi surface

```latex
\section{Trace sum rule on an isotropic Fermi surface}
\label{sec:isoT0}

\subsection{Derivation}

Summing Eq.~\eqref{eq:chiO-T0} (with $O=\sigma_{\mu}$) over $\mu$, and using Eq.~\eqref{eq:spin-total} at each $\mathbf{k}$,
\begin{equation}
	\mathrm{Tr}\,\chi(0)=\mu_{B}^{2}\sum_{\mathbf{k}}\sum_{s_{1}s_{2}}\frac{6-\sum_{\mu}\sum_{s_{1}'s_{2}'}|M_{ph,\mu}^{s_{1}'s_{2}'}(\mathbf{k})|^{2}}{E_{\mathbf{k}s_{1}}+E_{-\mathbf{k}s_{2}}}.
	\label{eq:trace-identity}
\end{equation}
On a 3D spherical FS, $\mathrm{Tr}\,\chi(T_{c})=3\chi_{N}=6\mu_{B}^{2}N(0)$. Converting the $\mathbf{k}$-sum to an FS integration with DOS $N(0)$ and using $\langle\cos^{2}\theta_{\mathbf{k}}\rangle=1/3$,
\begin{equation}
	\boxed{\;\mathrm{Tr}\,\chi(0)\le\tfrac{2}{3}\mathrm{Tr}\,\chi(T_{c})=2\chi_{N}.\;}
	\label{eq:trace-bound}
\end{equation}
Equivalently, the Knight-shift deficit $\Delta K_{\mu\mu}(0)\equiv\chi_{N}-\chi_{\mu\mu}(0)$ obeys $\mathrm{Tr}\,\Delta K(0)\ge\chi_{N}$.

The $2/3$ prefactor above is specific to the spherical FS average. We therefore do not promote Eq.~\eqref{eq:trace-bound} to a universal shape-only formula for non-spherical FS. What is universal, and sufficient for the applications below, is the strong-locking identity of Sec.~\ref{sec:anisoT0}: for any FS and SOC texture,
\[
	\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}],\qquad \mathrm{Tr}\,\chi(0)=2\chi_{N},
\]
because $\mathrm{Tr}\,\Pi=1$. The 2D-Rashba cylindrical-FS example and the quasi-1D example in Sec.~\ref{sec:anisoT0} both realize this exact trace $2\chi_{N}$ despite their different geometries.

Inequality~\eqref{eq:trace-bound} is pairing-symmetry-independent, SOC-strength-independent, and Zeeman-field-independent within the single-band unitary BdG framework whose transition at the measurement field is continuous~\cite{Maki1964,Clogston1962,Chandrasekhar62}. Violation signals breakdown of at least one of those assumptions (multi-orbital physics, non-unitary triplet, first-order transition, mixed-parity pairing, FFLO~\cite{FF_state,LO_state}, pair-density-wave order~\cite{PDW}, or strong correlations beyond mean field).

\subsection{Saturation pattern}

Table~\ref{tab:sat} collects $\mathrm{Tr}\,\chi(0)/\chi_{N}$ in the limiting cases reported in Ref.~\cite{pang2026}.

\begin{table}[b]
	\caption{Saturation of the trace bound $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$. Components in units of $\chi_{N}$.}
	\label{tab:sat}
	\renewcommand\arraystretch{1.3}
	\setlength{\tabcolsep}{0.6ex}
	\begin{tabular}{l|ccc|c}
		\hline\hline
		Pairing / limit & $\chi_{xx}(0)$ & $\chi_{yy}(0)$ & $\chi_{zz}(0)$ & Tr$/\chi_{N}$\\
		\hline
		$s$-wave, $g=\mathbf{H}=0$ & $0$ & $0$ & $0$ & $0$\\
		$s$-wave, $gk_{F}\!\gg\!\Delta$ & $2/3$ & $2/3$ & $2/3$ & $2$\\
		OSP ($\mathbf{d}\!\parallel\!\hat z$), $g=\mathbf{H}=0$ & $1$ & $1$ & $0$ & $2$\\
		ESP ($\mathbf{d}\!\in\!xy$), $g=\mathbf{H}=0$ & $1/2$ & $1/2$ & $1$ & $2$\\
		any unitary $p$-wave, $gk_{F}\!\gg\!\Delta$ & $2/3$ & $2/3$ & $2/3$ & $2$\\
		\hline\hline
	\end{tabular}
\end{table}

Every unitary triplet~\cite{AndersonandMorel1961,AndersonandBrinkman1973} saturates the bound already at $g=\mathbf{H}=0$. Strong Rashba SOC drives every pairing to $\chi_{\mu\mu}(0)\to(2/3)\chi_{N}$~\cite{Samokhin2007}. The only strict case is spin-singlet with weak SOC, made explicit in Sec.~\ref{sec:intermediate}.
```

## §5 Anisotropic identity

```latex
\section{Anisotropic identity for a general Fermi surface and SOC}
\label{sec:anisoT0}

\subsection{Normal-state benchmark at $T_{c}$}

At $T_{c}^{+}$, the intra-band and inter-band spin matrix elements read
\begin{align}
	\sum_{s}|(u^{\dagger}\sigma_{\mu}u)^{ss}|^{2}&=2(\hat n_{\mathbf{k}}\cdot\hat e_{\mu})^{2},\label{eq:me-intra}\\
	\sum_{s\ne s'}|(u^{\dagger}\sigma_{\mu}u)^{ss'}|^{2}&=2[1-(\hat n_{\mathbf{k}}\cdot\hat e_{\mu})^{2}],\label{eq:me-inter}
\end{align}
with the inter-band sum including both off-diagonal elements. Inserted into Eqs.~(13c)--(13d) of Ref.~\cite{pang2026} and evaluated with $-df/dE\to\delta(E)$,
\begin{equation}
	\chi^{ph+}_{\mu\mu}(T_{c})/\chi_{N}=\Pi_{\mu\mu},\qquad \chi^{ph-}_{\mu\mu}(T_{c})/\chi_{N}=1-\Pi_{\mu\mu}.
	\label{eq:phpartsTc}
\end{equation}
The two contributions add to $\chi^{ph}_{\mu\mu}(T_{c})=\chi_{N}$, so $\mathrm{Tr}\,\chi(T_{c})=3\chi_{N}$ for any FS and SOC.

\subsection{Strong-locking identity at $T=0$}

When $\mathbf{H}=0$ and $|\mathbf{g}_{\mathbf{k}}|\gg|\mathbf{d}(\mathbf{k})|,|\Delta|$ on the FS, the SOC splitting dominates; the intra-band pp term is negligible and the inter-band pp term gives twice Eq.~\eqref{eq:me-inter} with denominator $2|\mathbf{g}_{\mathbf{k}}|$. Phase-space cancellation identical to the normal-state computation yields
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}],\qquad\mathbf{H}=0,\;|\mathbf{g}_{\mathbf{k}}|/\Delta\to\infty.\;}
	\label{eq:strongSOCid}
\end{equation}
Consequences: trace universality $\mathrm{Tr}\,\chi(0)=2\chi_{N}$ for any FS/SOC; non-zero off-diagonal $\chi_{\mu\nu}(0)$ for tilted SOC; eigenvectors of $\Pi$ define spin-lock principal axes with $\pi_{1}+\pi_{2}+\pi_{3}=1$.

\subsection{Worked examples}

\emph{Isotropic 3D SOC.} $\Pi=\delta_{\mu\nu}/3$, $\chi_{\mu\nu}(0)=(2\chi_{N}/3)\delta_{\mu\nu}$~\cite{pang2026,Samokhin2007}.

\emph{2D Rashba, cylindrical FS.} $\Pi=\mathrm{diag}(1/2,1/2,0)$, $\chi_{xx}=\chi_{yy}=\chi_{N}/2$, $\chi_{zz}=\chi_{N}$.

\emph{Quasi-1D SOC along a chain.} $\Pi=\mathrm{diag}(0,0,1)$, $\chi_{xx,yy}=\chi_{N}$, $\chi_{zz}=0$.

\emph{Tilted texture.} $\mathbf{g}_{\mathbf{k}}=k_{x}(\alpha\hat x+\beta\hat z)$ yields $\Pi_{xz}\neq 0$, accessible as an off-diagonal Knight-shift tensor element $K_{xz}$.

\subsection{Unified formulation with zero-SOC unitary triplets}

Replacing $\hat n_{\mathbf{k}}\to\hat d_{\mathbf{k}}=\mathbf{d}/|\mathbf{d}|$, the same derivation at zero SOC for a fully gapped unitary triplet~\cite{Leggett1975,Sigrist1991} yields
\begin{equation}
	\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi^{(d)}_{\mu\nu}],\quad \Pi^{(d)}_{\mu\nu}=\langle\hat d_{\mu}\hat d_{\nu}\rangle_{\rm FS}.
	\label{eq:strong-triplet}
\end{equation}
Equations~\eqref{eq:strongSOCid} and~\eqref{eq:strong-triplet} unify as
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0)/\chi_{N}=\delta_{\mu\nu}-\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS},\;}
	\label{eq:unified}
\end{equation}
with $\hat n$ the dominant locking vector ($\hat g_{\mathbf{k}}$, $\hat d_{\mathbf{k}}$, or normalized $\mu_{B}\mathbf{H}+\mathbf{g}_{\mathbf{k}}$ in the respective limits). This single identity underlies every geometric diagnostic in Part~II.
```

## §6 Intermediate-SOC interpolation

```latex
\section{Intermediate-SOC interpolation for $s$-wave pairing}
\label{sec:intermediate}

At zero Zeeman field, the anisotropic identity Eq.~\eqref{eq:unified} admits an exact closed-form interpolation across all SOC strengths for $s$-wave pairing.

\subsection{Reduction to a single integral}

From Eq.~(23c) of Ref.~\cite{pang2026},
\begin{equation}
	\chi_{\mu\nu}(0)=\tfrac{\chi_{N}}{2}\langle[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\tilde J(\lambda_{\mathbf{k}})\rangle_{\rm FS},\quad \tilde J(\lambda)=\int_{-\infty}^{\infty}d\xi\,\mathcal{F}(\xi,\lambda\Delta,\Delta),
	\label{eq:chi-FSaverage}
\end{equation}
with $\mathcal{F}(\xi,\alpha,\Delta)=[E_{+}E_{-}-\xi_{+}\xi_{-}-\Delta^{2}]/[E_{+}E_{-}(E_{+}+E_{-})]$, $\xi_{\pm}=\xi\pm\alpha$, $E_{\pm}=\sqrt{\xi_{\pm}^{2}+\Delta^{2}}$, and $\lambda_{\mathbf{k}}=|\mathbf{g}_{\mathbf{k}}|/\Delta$.

\subsection{Closed-form evaluation}
\label{sec:intermediate-closed}

An ellipse parametrization $u=\xi/\Delta$, $a=(f+g)/2$ with $f=\sqrt{(u+\lambda)^{2}+1}$, $g=\sqrt{(u-\lambda)^{2}+1}$ gives the identity $fg-u^{2}+\lambda^{2}-1=2\lambda^{2}/(a^{2}-\lambda^{2})$. Evaluation yields
\begin{equation}
	\boxed{\;F_{s}(\lambda)\equiv\tfrac{1}{2}\tilde J(\lambda)=1-\frac{\sinh^{-1}\lambda}{\lambda\sqrt{1+\lambda^{2}}},\;}
	\label{eq:Fs}
\end{equation}
and
\begin{equation}
	\boxed{\;\frac{\chi_{\mu\nu}(0)}{\chi_{N}}=\langle F_{s}(\lambda_{\mathbf{k}})[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\rangle_{\rm FS}.\;}
	\label{eq:chi-explicit}
\end{equation}

\subsection{Properties of $F_{s}$}

$F_{s}(0)=0$, $F_{s}(\infty)=1$, monotonic. Small-$\lambda$: $F_{s}=\tfrac{2}{3}\lambda^{2}-\tfrac{8}{15}\lambda^{4}+O(\lambda^{6})$. Large-$\lambda$: $F_{s}=1-\ln(2\lambda)/\lambda^{2}+\cdots$. Benchmarks: $F_{s}(1)=0.377$, $F_{s}(2)=0.677$, $F_{s}(5)=0.909$; half-saturation at $\lambda\approx 1.317$.

\subsection{Trace form and SOC spectroscopy}

$\mathrm{Tr}\,\chi(0)/\chi_{N}=2\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}\le 2$, strict for finite SOC. For uniform SOC the relation is invertible: $\lambda=F_{s}^{-1}(\mathrm{Tr}\,\chi(0)/2\chi_{N})$, yielding a pair-breaking spectroscopy of $|\mathbf{g}|/\Delta$ from three-axis Knight shift (deployed as Protocol~B in Sec.~\ref{sec:protocols}).

\subsection{Numerical cross-check against published Fig.~3}

Extracting the $T=0$ intercepts of the five $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}, labeled by $gk_{F}/(k_{B}T_{c0})=0,1,2,4,30$, and converting via BCS $\Delta_{0}/(k_{B}T_{c0})=\pi/e^{\gamma_{E}}=1.7638769\ldots$,
\begin{equation}
	\chi(0)/\chi_{N}=\tfrac{2}{3}F_{s}(gk_{F}/(k_{B}T_{c0})\cdot e^{\gamma_{E}}/\pi),
	\label{eq:fig3-crosscheck}
\end{equation}
yields the overlay in Fig.~\ref{fig:fig3-t0-validation}: max deviation $1.5\times 10^{-3}$ in $\chi/\chi_{N}$, RMS $7.7\times 10^{-4}$.

\begin{figure}[t]
	\centering
	\includegraphics[width=0.62\linewidth]{figures/fig3_t0_validation}
	\caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
	\label{fig:fig3-t0-validation}
\end{figure}

\subsection{Heuristic extension to unitary triplet with anisotropic gap}

Replacing $\Delta\to|\mathbf{d}(\mathbf{k})|$ in the $\xi$-integration suggests the ansatz $F_{\rm t}(\lambda_{\mathbf{k}})\approx F_{s}(|\mathbf{g}_{\mathbf{k}}|/|\mathbf{d}(\mathbf{k})|)$, with $F_{\rm t}\to 1$ at nodes. This captures the gap-magnitude dependence exactly when the pairing amplitude is spatially constant across the FS, but misses corrections from the $\hat d$-vector angular structure and from intra-band triplet channels. A rigorous derivation is beyond the present scope.
```

Continuing with §7 (finite-H), §8 (spin-FGT), §9 (multi-band) next; let me know if you want any adjustments to what I've produced so far before I go on.

---
## 🧑‍💻 User

go ahead, pls

---
## 🤖 Assistant

## §7 Strong-locking identity at finite Zeeman field

```latex
\section{Strong-locking identity at finite Zeeman field}
\label{sec:finiteH}

The anisotropic identity Eq.~\eqref{eq:unified} was derived at $\mathbf{H}=0$. NMR experiments are necessarily conducted at finite field, typically with $\mu_B H$ comparable to $\Delta$, so an extension is required. In this section we show that Eq.~\eqref{eq:unified} survives at finite $\mathbf{H}$ in the strong-locking regime $|\mathbf{b}_{\mathbf{k}}|\gg\Delta$, with a field-dependent projection tensor $\Pi(\mathbf{H})$; we quantify the leading corrections and delineate the regimes in which a closed form is inaccessible. Throughout this section we use the dimensionless ratios $\lambda\equiv|\mathbf{g}_{\mathbf{k}}|/\Delta$ and $h\equiv\mu_{B}|\mathbf{H}|/\Delta$.

\subsection{Structure of the finite-field problem}

With both fields present, the normal-state quasiparticle spin is locked along the composite vector
\begin{equation}
	\mathbf{b}_{\mathbf{k}}=\mu_B\mathbf{H}+\mathbf{g}_{\mathbf{k}},\qquad \hat n_{\mathbf{k}}(\mathbf{H})=\mathbf{b}_{\mathbf{k}}/|\mathbf{b}_{\mathbf{k}}|.
	\label{eq:bvec}
\end{equation}
For Rashba-type SOC with $\mathbf{g}_{-\mathbf{k}}=-\mathbf{g}_{\mathbf{k}}$,
\begin{equation}
	|\mathbf{b}_{\mathbf{k}}|^2-|\mathbf{b}_{-\mathbf{k}}|^2=4\mu_B\mathbf{H}\cdot\mathbf{g}_{\mathbf{k}},
	\label{eq:asymmetry}
\end{equation}
so any Zeeman component parallel to $\mathbf{g}_{\mathbf{k}}$ breaks the Kramers symmetry of Cooper pairs. A direct characteristic-polynomial check shows that the simple two-sector factorization of the $4\times 4$ BdG matrix occurs in the \emph{collinear} case $\mathbf{H}\parallel\mathbf{g}_{\mathbf{k}}$; a noncollinear configuration retains the generic quartic structure. Accordingly, no closed-form expression for $\chi_{\mu\nu}(0,\mathbf{H})$ is available at generic $(\mathbf{H},\mathbf{g}_{\mathbf{k}},\Delta)$. What survives analytically is the strong-locking regime.

\subsection{Strong-locking identity at finite $\mathbf{H}$}

When the minimum locking magnitude over the FS satisfies
\begin{equation}
	b_{\min}(\mathbf{H})\equiv\min_{\mathbf{k}\in\rm FS}|\mathbf{b}_{\mathbf{k}}|\;\gg\;\Delta,
	\label{eq:strong-locking-H}
\end{equation}
the quasiparticle denominators $E_{\mathbf{k}s_1}+E_{-\mathbf{k}s_2}$ are dominated by the band-splitting energy $2b_{\mathbf{k}}$, and the intra-band pp contribution is $O(\Delta^2/b^2)$ and negligible. The inter-band pp contribution reproduces the matrix-element structure of Eq.~\eqref{eq:me-inter} with the zero-field locking vector replaced by the field-dependent one in Eq.~\eqref{eq:bvec}. Phase-space cancellation identical to the normal-state calculation of Sec.~\ref{sec:anisoT0} then yields
\begin{equation}
	\boxed{\;\chi_{\mu\nu}(0,\mathbf{H})=\chi_N\big[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})\big]+O\!\big(\Delta^2/b_{\min}^2\big),\;}
	\label{eq:strongH-identity}
\end{equation}
with the field-dependent projection tensor
\begin{equation}
	\Pi_{\mu\nu}(\mathbf{H})\equiv\big\langle\hat n_{\mu}(\mathbf{k};\mathbf{H})\,\hat n_{\nu}(\mathbf{k};\mathbf{H})\big\rangle_{\rm FS}.
	\label{eq:Pi-H}
\end{equation}
As the applied field is varied, the Knight-shift ellipsoid deforms continuously, always lying on the simplex $\sum_i\pi_i(\mathbf{H})=1$ to leading order. The trace is universal,
\begin{equation}
	\mathrm{Tr}\,\chi(0,\mathbf{H})=2\chi_N\big[1+O(\Delta^2/b_{\min}^2)\big],
	\label{eq:trace-H}
\end{equation}
field-independent to leading order in the strong-locking regime. The ellipsoid theorem of Sec.~\ref{sec:ellipsoid} thereby generalizes to finite field: the rotation components of the Knight-shift tensor at $T=0$ determine $\Pi(\mathbf{H})$ directly.

\subsection{Worked limits}

\emph{(a) Weak Zeeman on top of strong SOC.} For $\mu_B H\ll|\mathbf{g}_{\mathbf{k}}|$, i.e., $h\ll\lambda$, expansion of $\hat n_{\mathbf{k}}(\mathbf{H})$ in powers of $h/\lambda$ gives odd powers of $\mathbf{H}$ that vanish on FS averaging by the parity $\hat g_{-\mathbf{k}}=-\hat g_{\mathbf{k}}$ of Rashba-type SOC. The leading correction is therefore quadratic,
\begin{equation}
	\Pi_{\mu\nu}(\mathbf{H})=\Pi_{\mu\nu}(0)+O(h^2/\lambda^2),
	\label{eq:Pi-H-weak}
\end{equation}
and the zero-field ellipsoid is \emph{stable} against small applied fields. Practically, the zero-field diagnostic of Sec.~\ref{sec:ellipsoid} applies without modification at measurement fields $H\ll g k_F/\mu_B$.

\emph{(b) Zeeman-dominated locking.} For $\mu_B H\gg|\mathbf{g}_{\mathbf{k}}|$ on the FS, $\hat n_{\mathbf{k}}\to\hat{\mathbf{H}}$ uniformly, $\Pi(\mathbf{H})\to\hat{\mathbf{H}}\otimes\hat{\mathbf{H}}$, and
\begin{equation}
	\chi_{\mu\nu}(0,\mathbf{H})\to\chi_N[\delta_{\mu\nu}-\hat H_{\mu}\hat H_{\nu}],
	\label{eq:strongZeeman}
\end{equation}
an oblate-axial ellipsoid with symmetry axis along $\hat{\mathbf{H}}$: the longitudinal direction collapses while the two transverse directions respond at $\chi_N$. Physically, this is the field-aligned analogue of an OSP state with $\mathbf{d}\parallel\hat{\mathbf{H}}$.

\emph{(c) Vanishing locking (breakdown).} If $|\mathbf{b}_{\mathbf{k}_0}|\to 0$ at some $\mathbf{k}_0$ on the FS, the condition Eq.~\eqref{eq:strong-locking-H} is violated and Eq.~\eqref{eq:strongH-identity} fails locally. For 3D Rashba with $\mathbf{H}\parallel\hat z$ and spherical FS, this occurs at the critical field
\begin{equation}
	\mu_B H^{\ast}=g k_F,
	\label{eq:Hstar}
\end{equation}
where SOC and Zeeman contributions cancel at a pole of the FS. At $H^{\ast}$ a Bogoliubov Fermi surface forms~\cite{pang2026}, and the full numerical BdG solution is required. The kinks reported in Fig.~5(a) of Ref.~\cite{pang2026} locate this breakdown and its successors.

\subsection{Regime diagram and limitations}

The strong-locking regime Eq.~\eqref{eq:strong-locking-H} for Rashba SOC with $\mathbf{H}\parallel\hat z$ and spherical FS becomes
\begin{equation}
	|g k_F-\mu_B H|\gg\Delta,
	\label{eq:strong-locking-criterion}
\end{equation}
valid both at low field ($\mu_B H\ll gk_F$, covered by Eq.~\eqref{eq:Pi-H-weak}) and high field ($\mu_B H\gg gk_F$, Eq.~\eqref{eq:strongZeeman}), but not in the crossover window around $H^{\ast}$. Outside the strong-locking regime, no closed form is known. We verified numerically that naive substitutions such as $\Delta\to\sqrt{\Delta^2-(\mu_B H)^2}$ in Eq.~\eqref{eq:chi-explicit} do not reproduce the self-consistent BdG result, departing by $O(1)$ in $\chi/\chi_N$ across the bulk of the $(g,H)$ phase diagram; the problem is structural (the BdG fails to block-diagonalize) rather than a matter of substitution.
```

## §8 Spin FGT sum rule

```latex
\section{Spin analogue of the Ferrell--Glover--Tinkham sum rule}
\label{sec:spinFGT}

The results so far concern the static ($\omega=0$) spin susceptibility. A complementary identity constrains the \emph{dynamical} response: whatever Knight-shift deficit is produced by pair formation must reappear as additional spectral weight at finite frequency in $\mathrm{Im}\,\chi_{\mu\mu}(\omega)$. We state this identity, trace its origin to the generalized sum rule of Sec.~\ref{sec:generalized}, and discuss its relation to the spin-lattice relaxation rate $1/T_{1}$.

\subsection{Spectral sum rule}

The uniform spin susceptibility satisfies Kramers--Kronig at $\omega=0$ in both the normal and superconducting states:
\begin{equation}
	\chi_{\mu\mu}(T)=\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\mathrm{Im}\,\chi_{\mu\mu}(\omega,T),
	\label{eq:KK}
\end{equation}
with $\mathrm{Im}\,\chi_{\mu\mu}(\omega)$ odd in $\omega$. Subtracting the two,
\begin{equation}
	\boxed{\;\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\big[\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)-\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega)\big]=\chi_{N}-\chi_{\mu\mu}(0)=\chi_{N}\pi_{\mu},\;}
	\label{eq:spinFGT}
\end{equation}
where $\chi_{\mu\mu}(0)=\chi_{N}(1-\pi_{\mu})$ is the strong-locking identity Eq.~\eqref{eq:unified}. Equation~\eqref{eq:spinFGT} is the spin analogue of the Ferrell--Glover--Tinkham optical sum rule: \emph{the weighted spectral weight removed from the superconducting state at each frequency equals the Knight-shift deficit}, itself a geometric quantity determined by the FS average $\Pi_{\mu\mu}=\langle(\hat n\cdot\hat e_{\mu})^{2}\rangle_{\rm FS}$.

\subsection{Origin in the generalized sum rule}

Equation~\eqref{eq:spinFGT} traces to Eq.~\eqref{eq:general-sum-rule} through the spectral representation of $\chi_{\mu\mu}$. In the SC state at $T=0$, only the pp channels contribute:
\begin{equation}
	\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega>0)=\pi\mu_{B}^{2}\sum_{\mathbf{k},s_{1}s_{2}}|M_{pp,\mu}^{s_{1}s_{2}}(\mathbf{k})|^{2}\,\delta\!\big(\omega-E_{\mathbf{k}s_{1}}-E_{-\mathbf{k}s_{2}}\big).
	\label{eq:ImchiSC}
\end{equation}
In the normal state at $T_{c}^{+}$, only the ph channel contributes, with spectral support at the interband splitting $2|\mathbf{b}_{\mathbf{k}}|$ (Van Vleck) and a Landau damping contribution at $\omega\to 0$ (Pauli). Equation~\eqref{eq:general-sum-rule} fixes the \emph{total} squared matrix-element weight,
\begin{equation}
	\sum_{s_{1}s_{2}}\big[|M_{ph,\mu}|^{2}+|M_{pp,\mu}|^{2}\big]=2,
	\label{eq:total-weight}
\end{equation}
per $\mathbf{k}$, so the \emph{total} oscillator strength, suitably weighted, is conserved across the superconducting transition. Spectral weight originally in the Pauli term at $\omega=0$ in the normal state is partially transferred into a continuum above $\omega=2\Delta_{\min}$ in the SC state, with the missing static response set by $\pi_{\mu}$.

\subsection{Physical content: spectral-weight transfer}

Figure~\ref{fig:spinFGT-spectral} sketches the ph and pp pieces of the spectral function. In the normal state, the Pauli component appears at $\omega\to 0$ (Landau-broadened at finite $T$), with Van Vleck weight at the SOC-induced interband threshold. In the SC state, the $\omega\to 0$ weight is reduced by the factor $1-\pi_{\mu}$, and the displaced weight reappears above $2\Delta_{\min}$ as pair-breaking absorption. The total integrated $\mathrm{Im}\,\chi/\omega$ is preserved.

\begin{figure}[t]
	\centering
	\begin{tikzpicture}[scale=0.9]
		\draw[->] (0,0) -- (7,0) node[right] {$\omega$};
		\draw[->] (0,0) -- (0,3) node[above] {$\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$};
		\draw[thick,blue] (0,0) -- (0.02,2.6);
		\draw[thick,blue] (0.02,2.6) -- (0.2,0.2);
		\draw[thick,blue] (0.2,0.2) -- (4,0.2) .. controls (4.5,0.5) and (5,0.5) .. (5.5,0.2) -- (7,0.2);
		\node[blue] at (1,2.3) {\footnotesize normal};
		\draw[thick,red,dashed] (0,0) -- (0.02,1.4);
		\draw[thick,red,dashed] (0.02,1.4) -- (0.2,0.1);
		\draw[thick,red,dashed] (0.2,0.1) -- (2.5,0.1);
		\draw[thick,red,dashed] (2.5,0.1) .. controls (3,0.8) and (3.5,0.9) .. (4.5,0.6) .. controls (5.2,0.4) and (6,0.3) .. (7,0.25);
		\node[red] at (4.5,1.1) {\footnotesize SC};
		\draw[dashed,gray] (2.5,0) -- (2.5,1);
		\node[below] at (2.5,-0.05) {\footnotesize $2\Delta_{\min}$};
		\draw[<->, thick, black] (-0.4,1.4) -- (-0.4,2.6);
		\node[left] at (-0.4,2.0) {\footnotesize $\chi_N\pi_\mu$};
	\end{tikzpicture}
	\caption{Schematic: $\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$ in the normal state (blue) and the SC state (red). Spectral weight of magnitude $\chi_{N}\pi_{\mu}$ is transferred from the static peak at $\omega\to 0$ into the pair-breaking continuum above $2\Delta_{\min}$, conserving the Kramers--Kronig integral Eq.~\eqref{eq:spinFGT}. The Van Vleck bump at the interband threshold is essentially unaffected by pairing at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$.}
	\label{fig:spinFGT-spectral}
\end{figure}

Two limits make the geometric content explicit:

\emph{(a) Strong SOC, $s$-wave, spherical FS}: $\pi_{\mu}=1/3$, so $\chi_{N}\pi_{\mu}=\chi_{N}/3$. One third of the Pauli spectral weight is transferred to the pair-breaking continuum; two thirds remain at $\omega=0$ as the Van Vleck-like residual Knight shift.

\emph{(b) Unitary triplet with $\hat d\parallel\hat z$, zero SOC}: $\pi_{z}=1$, so the entire longitudinal spectral weight is transferred; $\chi_{zz}(0)=0$.

\subsection{Relation to the spin-lattice relaxation rate $1/T_{1}$}

The spin-lattice relaxation rate probes a different slice of $\mathrm{Im}\,\chi$. In the Moriya expression~\cite{tinkham,Triplet2021},
\begin{equation}
	\frac{1}{T_{1}T}=\gamma_{n}^{2}k_{B}\sum_{\mathbf{q}}|A_{\rm hf}(\mathbf{q})|^{2}\lim_{\omega\to 0}\frac{\mathrm{Im}\,\chi_{+-}(\mathbf{q},\omega)}{\omega},
	\label{eq:T1}
\end{equation}
$1/T_{1}$ measures the low-$\omega$ limit of $\mathrm{Im}\chi_{+-}$, integrated over $\mathbf{q}$ with the hyperfine form factor. The spin-FGT sum rule Eq.~\eqref{eq:spinFGT}, in contrast, integrates over $\omega$ at $\mathbf{q}=0$. These two quantities probe orthogonal slices of the full spectral function $\mathrm{Im}\,\chi_{\mu\mu}(\mathbf{q},\omega)$, so no exact equality follows from Eq.~\eqref{eq:spinFGT} alone.

Three quantitative statements do follow, and constitute the experimental utility of the framework.

\emph{(i) Oscillator-strength budget.} The total $\mathbf{q}=0$ spectral weight available for transfer into $1/T_{1}$ is bounded by $\chi_{N}\pi_{\mu}$. The $\mathbf{q}=0$ piece of $1/T_{1}$ cannot exceed this budget.

\emph{(ii) Sub-gap suppression (heuristic bound).} Under the hypothesis that $\mathrm{Im}\chi_{+-}(\mathbf{q},\omega)/\omega$ is dominated by $\mathbf{q}\approx 0$---valid when the hyperfine form factor $|A_{\rm hf}(\mathbf{q})|^{2}$ varies slowly and when magnetic correlations are not peaked at finite $\mathbf{q}$---the integrated $1/T_{1}$ deficit from pairing satisfies
\begin{equation}
	\int_{0}^{T_{c}}\!\frac{dT}{T}\Big[\frac{1}{T_{1}^{N}(T)}-\frac{1}{T_{1}^{SC}(T)}\Big]\;\lesssim\;\gamma_{n}^{2}k_{B}\,\langle|A_{\rm hf}|^{2}\rangle\,\chi_{N}\pi_{\mu}.
	\label{eq:T1-bound}
\end{equation}
Equation~\eqref{eq:T1-bound} is a heuristic \emph{budget} statement. What is rigorous is the saturation condition: Eq.~\eqref{eq:T1-bound} is saturated only when $1/T_{1}$ is $\mathbf{q}\approx 0$-dominated. A measured deficit \emph{larger} than the RHS is a direct, unambiguous diagnostic of finite-$\mathbf{q}$ dominance in the spin-fluctuation spectrum. The RHS is fixed by the Knight-shift diagnostic of Sec.~\ref{sec:ellipsoid}, with no remaining freedom.

\emph{(iii) Coherence-peak sign.} The Hebel--Slichter coherence peak immediately below $T_{c}$ is the signature of low-energy spectral weight concentrated near $\omega\approx 2\Delta$, constructive for $s$-wave and destructive for sign-changing pairings~\cite{Leggett1975,AndersonandMorel1961}. A vanishing coherence peak indicates that the $\chi_{N}\pi_{\mu}$ spectral weight has been transferred to frequencies $\gtrsim 2\Delta$ rather than piling up at the gap edge, a geometric statement that complements the standard pairing-symmetry argument.
```

## §9 Multi-band extension

```latex
\section{Multi-band extension}
\label{sec:multiband}

\subsection{Disjoint-pocket form}

For $N_{b}$ disjoint FS pockets, additivity of the Kubo expression gives
\begin{equation}
	\chi_{\mu\nu}(0)=\sum_{i}\chi_{N}^{(i)}[\delta_{\mu\nu}-\Pi^{(i)}_{\mu\nu}],
	\label{eq:multiband-id}
\end{equation}
with $\chi_{N}=\sum_{i}\chi_{N}^{(i)}=\mathrm{Tr}\,\chi(T_{c})/3$ and
\begin{equation}
	\boxed{\;\mathrm{Tr}\,\chi(0)\le 2\sum_{i}\chi_{N}^{(i)}=\tfrac{2}{3}\mathrm{Tr}\,\chi(T_{c}).\;}
	\label{eq:multiband-bound}
\end{equation}

\subsection{Inter-band mixing}

Equation~\eqref{eq:multiband-id} neglects inter-band pairing (exact for orbital-diagonal pairing). For orbitally mixed pairing, the formula is a decoupled-pocket baseline; deviations diagnose the inter-band structure. The Plancherel identity Eq.~\eqref{eq:general-sum-rule} itself is independent of the orbital-diagonal assumption; it is the specific anisotropic identity that requires the decoupled-pocket setting. A dedicated multi-orbital derivation is required before importing the simplex interpretation of Part~II to genuine inter-band pairing; the experimental bound Eq.~\eqref{eq:site-bound} and the trace inequality Eq.~\eqref{eq:multiband-bound} remain valid regardless.

\subsection{Structural prediction for A$_{2}$Cr$_{3}$As$_{3}$}
\label{sec:multiband-A2Cr3As3}

Density-functional calculations~\cite{Jiang15,Wu15} give three FS bands in the A$_{2}$Cr$_{3}$As$_{3}$ family (A=Na,K,Rb,Cs)~\cite{Bao15,Tang15_1,Tang15_2,Mu18,ZHOU2017208}: quasi-1D bands $\alpha,\beta$ and a 3D band $\gamma$, with DOS fractions $w_{\alpha,\beta,\gamma}$ satisfying $\sum w_i=1$. Under a $P\bar 6 m 2$-consistent SOC texture, the quasi-1D bands have $\hat n^{(\alpha,\beta)}\approx\mathrm{sgn}(k_z)\hat c$, giving $\Pi^{(\alpha,\beta)}\approx\mathrm{diag}(0,0,1)$, while the 3D $\gamma$ pocket, \emph{if} it carries an approximately isotropic Rashba SOC $\mathbf{g}_{\mathbf{k}}\propto\mathbf{k}$, gives $\Pi^{(\gamma)}\approx\mathrm{diag}(1/3,1/3,1/3)$. Substituting into Eq.~\eqref{eq:multiband-id},
\begin{equation}
	\frac{\chi_{\mu\nu}(0)}{\chi_{N}}=\delta_{\mu\nu}-\left[w_{\parallel}\,\mathrm{diag}(0,0,1)_{\mu\nu}+\tfrac{w_{\gamma}}{3}\delta_{\mu\nu}\right],
	\label{eq:a2cr3as3-pred}
\end{equation}
with $w_{\parallel}=w_{\alpha}+w_{\beta}=1-w_{\gamma}$. Component-wise,
\begin{align}
	\chi_{xx}(0)/\chi_{N}=\chi_{yy}(0)/\chi_{N} &=\tfrac{2}{3}+\tfrac{1}{3}w_{\parallel},\label{eq:a2cr3as3-perp}\\
	\chi_{zz}(0)/\chi_{N} &=\tfrac{2}{3}(1-w_{\parallel}).\label{eq:a2cr3as3-par}
\end{align}
Equations~\eqref{eq:a2cr3as3-perp}--\eqref{eq:a2cr3as3-par} define a one-parameter family traced by $w_{\parallel}$. As $w_{\parallel}$ increases from $0$ (all weight on the isotropic 3D band) to $1$ (all weight on the quasi-1D bands), the predicted point $(\pi_{a},\pi_{b},\pi_{c})$ moves from the barycenter $(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$ to the vertex $(0,0,1)$ of the simplex of Part~II (Fig.~\ref{fig:simplex}). A quantitative comparison with K$_{2}$Cr$_{3}$As$_{3}$ data is given in Sec.~\ref{sec:K2Cr3As3}.
```

## Part II bridge + §10 Ellipsoid theorem

```latex
\section*{Bridge: from identities to measurement}
\addcontentsline{toc}{section}{Bridge: from identities to measurement}

The remaining sections convert the identities of Part~I into experimental practice. The central geometric observation is that the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is a linear map from a symmetric traceful tensor ($\Pi$, $\mathrm{Tr}\,\Pi=1$) to a measurable symmetric tensor ($K_{\mu\nu}(0)$). A single-crystal Knight-shift rotation at $T=0$ therefore determines $\Pi$ directly, no fitting parameters. The eigenvalues of $\Pi$ live on a two-dimensional simplex, and each vertex, edge, and interior point corresponds to a distinct pairing class. Section~\ref{sec:ellipsoid} states this diagnostic. Section~\ref{sec:protocols} packages it, together with the finite-field, dynamical ($1/T_1$), site-resolved, and multi-band content of Part~I, into six experimental protocols. Section~\ref{sec:K2Cr3As3} walks through K$_{2}$Cr$_{3}$As$_{3}$ as a worked example.

\section{Knight-shift ellipsoid and the simplex of pairing classes}
\label{sec:ellipsoid}

\subsection{Knight-shift tensor and ellipsoid representation}

For scalar hyperfine coupling $A^{(\mathbf{R})}_{\mu\nu}=A^{(\mathbf{R})}\delta_{\mu\nu}$ (the default setting of this subsection), the spin part of the Knight-shift tensor at site $\mathbf{R}$ is linearly related to the electronic spin susceptibility~\cite{tinkham,Triplet2021}:
\begin{equation}
	K_{\mu\nu}(T)=A^{(\mathbf{R})}\chi_{\mu\nu}(T).
	\label{eq:Kdef}
\end{equation}
The dimensionless ratio $K_{\mu\nu}(T)/K_{\mu\nu}(T_{c})=\chi_{\mu\nu}(T)/\chi_{N}$ eliminates the hyperfine prefactor.

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

\subsection{Allowed shapes and the pairing-class catalogue}

The constraint $\pi_{1}+\pi_{2}+\pi_{3}=1$ with $0\le\pi_{i}\le 1$ confines the allowed ellipsoids to a two-dimensional simplex (Fig.~\ref{fig:simplex}). Each vertex, edge, and interior point corresponds to a distinct pairing class or locking-vector texture. Table~\ref{tab:ellipsoids} catalogues the canonical cases.

\begin{figure}[t]
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
		\node[below=3pt, align=center, font=\scriptsize] at (V1) {$(1,0,0)$\\ OSP $\mathbf{d}\|\hat a$\\ or quasi-1D $\|\hat a$};
		\node[below=3pt, align=center, font=\scriptsize] at (V2) {$(0,1,0)$\\ OSP $\mathbf{d}\|\hat b$\\ or quasi-1D $\|\hat b$};
		\node[above=3pt, align=center, font=\scriptsize] at (V3) {OSP $\mathbf{d}\|\hat c$\\ or quasi-1D $\|\hat c$\\ $(0,0,1)$};
		\node[align=center, font=\scriptsize, yshift=-36pt] at (M12) {$(\tfrac{1}{2},\tfrac{1}{2},0)$\\ ESP $\mathbf{d}\!\in\! ab$\\ or 2D Rashba in $ab$};
		\node[left=4pt, align=right, font=\scriptsize] at (M13) {$(\tfrac{1}{2},0,\tfrac{1}{2})$\\ ESP $\mathbf{d}\!\in\! ac$\\ or 2D Rashba in $ac$};
		\node[right=4pt, align=left, font=\scriptsize] at (M23) {$(0,\tfrac{1}{2},\tfrac{1}{2})$\\ ESP $\mathbf{d}\!\in\! bc$\\ or 2D Rashba in $bc$};
		\node[right=6pt, align=left, font=\scriptsize] at (B) {$(\tfrac{1}{3},\tfrac{1}{3},\tfrac{1}{3})$\\ singlet strong SOC\\ or isotropic 3D SOC};
		\draw[->, thick, blue!60!black, shorten >=1pt] ($(B)+(210:0.28)$) -- ($(B)+(210:0.02)$);
		\node[below left=1pt, font=\scriptsize, blue!60!black] at ($(B)+(210:0.28)$) {\shortstack[l]{intermediate\\SOC: $\langle F_s\rangle\!\uparrow$}};
	\end{tikzpicture}
	\caption{The simplex $\pi_{1}+\pi_{2}+\pi_{3}=1$, $\pi_{i}\in[0,1]$, of allowed $T=0$ Knight-shift ellipsoids in the strong-locking regime [Eq.~\eqref{eq:Kellipsoid}]. The three vertices (black) correspond to \emph{oblate axial} ellipsoids produced by OSP with $\mathbf{d}$ along a crystal axis, or equivalently by quasi-1D SOC along that axis: the response vanishes along that axis and is $K_{N}$ in the transverse plane. The three edge midpoints (red) correspond to \emph{prolate axial} ellipsoids produced by ESP with $\mathbf{d}$ in a crystal plane, or by 2D Rashba SOC confined to that plane: the response is $K_{N}$ along the normal axis and $K_{N}/2$ in the plane. The barycenter (blue) is the isotropic sphere, realized by $s$-wave pairing in the strong-SOC limit or by isotropic 3D SOC. Points in the interior correspond to tilted or anisotropic locking textures, for which all three principal values of $\Pi$ differ. In the intermediate-SOC regime, the effective-projection coordinates $p_{i}\equiv\mathrm{eig}\,\Pi^{\rm eff}$ contract radially from the strong-locking point toward the origin as the SOC weakens; for uniform SOC magnitude, $p_{i}=F_{s}(\lambda)\pi_{i}$.}
	\label{fig:simplex}
\end{figure}

\begin{table}[t]
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
\end{table}

Four observations make the table an experimental diagnostic.

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
\begin{equation}
	\sum_{i}\frac{K_{i}(0)}{K_{i}(T_{c}^{+})}=2,\qquad 0\le\frac{K_{i}(0)}{K_{i}(T_{c}^{+})}=1-\pi_{i}\le 1.
	\label{eq:Khf-trace}
\end{equation}
Non-coaxial hyperfine and susceptibility frames require an independent determination of $A$; we do not pursue that case here.

\subsection{Intermediate-SOC regime: ellipsoid contraction}

In the intermediate-SOC $s$-wave case of Eq.~\eqref{eq:chi-explicit}, the scalar-hyperfine Knight shift reads
\begin{equation}
	\frac{K(\hat{\mathbf{H}},0)}{K_{N}}=\big\langle F_{s}(\lambda_{\mathbf{k}})\big[1-(\hat{\mathbf{H}}\cdot\hat n_{\mathbf{k}})^{2}\big]\big\rangle_{\rm FS}
	\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
	\label{eq:K-intermediate}
\end{equation}
with $S(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$ and
\begin{equation}
	\Pi^{\rm eff}_{\mu\nu}(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS},\qquad \mathrm{Tr}\,\Pi^{\rm eff}=S(\lambda)\le 1.
	\label{eq:Pi-eff}
\end{equation}
For uniform SOC magnitude, $\Pi^{\rm eff}=F_{s}(\lambda)\Pi$, so $p_{i}=F_{s}(\lambda)\pi_{i}$: the strong-locking ellipsoid contracts homothetically toward the origin as the SOC weakens. Fig.~\ref{fig:simplex} shows the direction of this contraction.
```

Next: §11 Protocols, §12 K₂Cr₃As₃ (trimmed), §13 Summary. Sending in the next message.

---
## 🧑‍💻 User

continue

---
## 🤖 Assistant

## §11 Protocols

```latex
\section{Experimental protocols}
\label{sec:protocols}

This section collects six self-contained protocols that implement the identities of Part~I as concrete measurements. Table~\ref{tab:protocols} summarizes what each protocol measures, its output, its assumptions, and the signature of failure. The protocols are ordered from the lightest (a single three-axis Knight shift) to the most demanding (multi-site multi-field program).

\begin{table}[t]
	\caption{Summary of protocols. "3-axis $K$" means Knight shift measured with $\mathbf{H}$ along each of three orthogonal crystal axes; "rotation" means full angular scan sufficient to determine the $K_{\mu\nu}$ tensor.}
	\label{tab:protocols}
	\renewcommand\arraystretch{1.3}
	\setlength{\tabcolsep}{0.7ex}
	\begin{tabular}{l|l|l|l|l}
		\hline\hline
		Protocol & Measurement & Output & Key assumption & Failure signature\\
		\hline
		A: trace bound & 3-axis $K(T)$ & $R=\tfrac{1}{3}\sum r_{\alpha}\le\tfrac{2}{3}$ & 3D isotropic FS & $R>\tfrac{2}{3}$\\
		B: ellipsoid & rotation at $T\to 0$ & $(\pi_{1},\pi_{2},\pi_{3})$ on simplex & strong locking & $\sum\pi_{i}\ne 1$\\
		C: finite-$H$ texture & rotation at fixed $H$ & $\Pi(\mathbf{H})$ vs $\hat{\mathbf{H}}$ & $|gk_{F}-\mu_{B}H|\!\gg\!\Delta$ & kink near $H^{\ast}$\\
		D: $1/T_{1}$ budget & $1/T_{1}(T,\hat{\mathbf{H}})$ & $\mathbf{q}\!=\!0$ vs finite-$\mathbf{q}$ diagnosis & scalar hyperfine & deficit $>$ RHS of Eq.~\eqref{eq:T1-bound}\\
		E: site-resolved & $K$ at each nucleus & $R^{(\mathbf{R})}$ invariance & single-band unitary BdG & site-to-site disagreement\\
		F: pocket decomposition & $K$ vs pressure/doping & $w_{\parallel}$ from Eq.~\eqref{eq:a2cr3as3-par} & orbital-diagonal pairing & trajectory off Eq.~\eqref{eq:a2cr3as3-pred}\\
		\hline\hline
	\end{tabular}
\end{table}

\subsection{Protocol A: trace bound from three-axis Knight shift}
\label{sec:protocolA}

A minimal test of the single-band unitary BdG framework that needs only $K_{\alpha}(T)$ with $\mathbf{H}\parallel\hat\alpha$ for three orthogonal directions.

\begin{enumerate}
	\item Measure $K_{\alpha}(T)$ for $\alpha=a,b,c$; extract $\chi_{\alpha\alpha}(T)$ via the hyperfine tensor.
	\item Form $r_{\alpha}\equiv\chi_{\alpha\alpha}(0)/\chi_{\alpha\alpha}(T_{c}^{+})$.
	\item Compute $R=\tfrac{1}{3}\sum_{\alpha}r_{\alpha}$.
	\item Compare against $R\le 2/3$ [Eq.~\eqref{eq:trace-bound}] on a 3D isotropic FS; or against $\sum r_{\alpha}\le 2$ [Eq.~\eqref{eq:Khf-trace}] for the general FS.
	\item Compare the observed triple $(r_{a},r_{b},r_{c})$ against Table~\ref{tab:sat} to discriminate singlet vs OSP vs ESP and infer the $\mathbf{d}$-vector orientation.
\end{enumerate}
A violation $R>2/3$ signals breakdown of at least one assumption (multi-orbital physics, non-unitary triplet, first-order transition, mixed-parity pairing, FFLO, PDW, or strong correlations beyond mean field).

\subsection{Protocol B: full ellipsoid rotation and pairing-class diagnostic}
\label{sec:protocolB}

The pairing-class diagnostic of Sec.~\ref{sec:ellipsoid} requires a Knight-shift rotation on a single crystal.

\begin{enumerate}
	\item At $T>T_{c}$, measure $K(\hat{\mathbf{H}},T_{c}^{+})$ along independent directions prescribed by crystal symmetry (see below) to extract $K_{\mu\nu}(T_{c})$; for cubic or isotropic hyperfine, this is simply $K_{N}$.
	\item Cool to $T\ll T_{c}$; repeat to extract $K_{\mu\nu}(0)$.
	\item Diagonalize $K_{\mu\nu}(0)$ and extract principal axes and principal values $K_{i}(0)$.
	\item In the strong-locking scalar-hyperfine case, $\pi_{i}=1-K_{i}(0)/K_{N}$; for diagonal anisotropic hyperfine, $\pi_{i}=1-K_{i}(0)/K_{i}(T_{c}^{+})$ axis by axis.
	\item For intermediate-SOC $s$-wave data, compute $S=\tfrac{1}{2}\sum_{i}K_{i}(0)/K_{N}$ and $p_{i}=S-K_{i}(0)/K_{N}$, the eigenvalues of $\Pi^{\rm eff}$.
	\item Plot $(\pi_{1},\pi_{2},\pi_{3})$ on the simplex of Fig.~\ref{fig:simplex} (strong locking) or the contracted point $(p_{1},p_{2},p_{3})$ on the corresponding radial trajectory (intermediate SOC).
	\item Verify $\sum_{i}\pi_{i}=1$ [Eq.~\eqref{eq:trace-from-ellipsoid}] or $\sum_{i}p_{i}=S\le 1$ [Eq.~\eqref{eq:Pi-eff}].
\end{enumerate}
The number of rotation angles required matches the number of independent components of $K_{\mu\nu}(T)$ permitted by crystal symmetry: two for uniaxial (tetragonal, hexagonal, trigonal), three for orthorhombic, four for monoclinic, six for triclinic. The protocol is information-theoretically minimal at each level and requires no parametrization of temperature dependence, gap amplitude, or hyperfine strength.

For intermediate SOC, inversion of the trace $\mathrm{Tr}\,\chi(0)/\chi_{N}=2\langle F_{s}\rangle_{\rm FS}$ using Eq.~\eqref{eq:Fs} gives a direct spectroscopic readout of $|\mathbf{g}|/\Delta$ for uniform SOC magnitude.

\subsection{Protocol C: finite-field SOC-texture spectroscopy}
\label{sec:protocolC}

At finite field, the ellipsoid deforms according to Eq.~\eqref{eq:strongH-identity}; rotating $\hat{\mathbf{H}}$ at fixed $H$ traces a family of points on the simplex that is a parameter-free prediction once the SOC texture is known.

\begin{enumerate}
	\item Confirm the strong-locking regime by checking $|gk_{F}-\mu_{B}H_{\rm NMR}|\gg\Delta$ using an independent SOC estimate, or by observing no anomaly in $K(T)$ attributable to a Bogoliubov Fermi surface.
	\item Measure $K(\hat{\mathbf{H}},T\to 0,H_{\rm NMR})$ along independent directions; form $K_{\mu\nu}(0,H)$ and diagonalize.
	\item Extract $\pi_{i}(H)=1-K_{i}(0,H)/K_{N}$ and the eigenvector frame.
	\item Verify $\sum_{i}\pi_{i}(H)\approx 1$; deviations quantify the $\Delta^{2}/b_{\min}^{2}$ corrections and diagnose proximity to $H^{\ast}$.
	\item Rotate $\hat{\mathbf{H}}$ at fixed $H$: the family $\Pi(H\hat{\mathbf{H}})$ directly probes the SOC texture $\mathbf{g}_{\mathbf{k}}$ via Eq.~\eqref{eq:Pi-H}. In crystals with a single well-defined SOC texture, the rotation curve is predicted without free parameters.
	\item Across a pressure/composition sweep, the drift of $\Pi(\mathbf{H})$ on the simplex encodes the SOC-texture evolution; $\sum_{i}\pi_{i}<1$ signals breakdown of strong locking and BFS formation.
\end{enumerate}

\subsection{Protocol D: $1/T_{1}$ cross-check and finite-$\mathbf{q}$ diagnosis}
\label{sec:protocolD}

Combining Knight-shift geometry with $1/T_{1}$ along the same field orientations tests the $\mathbf{q}\approx 0$ spin-FGT budget of Eq.~\eqref{eq:T1-bound}.

\begin{enumerate}
	\item From Protocol~B, extract $(\pi_{a},\pi_{b},\pi_{c})$; this fixes the RHS of Eq.~\eqref{eq:T1-bound} component-by-component.
	\item Measure $1/T_{1}(T)$ with $\mathbf{H}$ along each principal axis. Evaluate the integral $\int_{0}^{T_{c}}(dT/T)[1/T_{1}^{N}-1/T_{1}^{SC}]$ along axis $\alpha$.
	\item Compare the integrated deficit against the RHS evaluated at $\pi_{\alpha}$:
	\begin{itemize}
		\item A saturated inequality indicates $\mathbf{q}\approx 0$ spectral dominance.
		\item A deficit significantly \emph{smaller} than the RHS indicates partial redistribution to finite $\mathbf{q}$.
		\item A deficit \emph{larger} than the RHS is a direct, unambiguous diagnostic of finite-$\mathbf{q}$ dominance in the spin-fluctuation spectrum. This is the most powerful use of Eq.~\eqref{eq:T1-bound}.
	\end{itemize}
	\item Note the presence/absence of a Hebel--Slichter peak as an independent check: a vanishing peak is consistent with spectral weight transfer to frequencies $\gtrsim 2\Delta$ rather than pile-up at the gap edge.
	\item In an intermediate-SOC regime, the $\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$ factor modifies the RHS by a common factor; the ratio of $1/T_{1}$ deficits across a pressure/composition sweep isolates this SOC-dependent rescaling.
\end{enumerate}

\subsection{Protocol E: site-resolved consistency across NMR nuclei}
\label{sec:protocolE}

The site-resolved bound Eq.~\eqref{eq:site-bound} is hyperfine-invariant: different nuclei in the same compound must yield the same normalized Knight-shift geometry. This is the strongest internal consistency check available from a single crystal.

\begin{enumerate}
	\item Identify all NMR-active nuclei with resolvable $K$ and acceptable signal-to-noise.
	\item Run Protocol~B at each nucleus independently; form $(\pi_{1},\pi_{2},\pi_{3})^{(\mathbf{R})}$.
	\item Compare across nuclei. Agreement to $\lesssim 5\%$ in every component (typical $T\to 0$ extrapolation resolution) is consistent with the single-band unitary BdG framework.
	\item A systematic discrepancy at the $10$--$20\%$ level indicates a subleading correction: inter-band parity mixing~\cite{Frigeri2004,bauer2012non,Samokhin2007}, a non-unitary triplet component with small $\mathbf{m}\propto i\mathbf{d}\times\mathbf{d}^{*}$, or a site-specific orbital contribution not captured by the common geometric kernel.
	\item A discrepancy $\gtrsim 50\%$ in any component is quantitative evidence that the single-band unitary BdG framework does not apply and a multi-orbital or multi-$\mathbf{d}$-vector extension is required.
\end{enumerate}

\subsection{Protocol F: multi-band pocket decomposition}
\label{sec:protocolF}

For materials with multiple FS pockets, the multi-band decomposition Eq.~\eqref{eq:multiband-id} admits a direct experimental test under the orbital-diagonal hypothesis. The application to A$_{2}$Cr$_{3}$As$_{3}$ with the textures of Sec.~\ref{sec:multiband-A2Cr3As3} gives Eqs.~\eqref{eq:a2cr3as3-perp}--\eqref{eq:a2cr3as3-par}.

\begin{enumerate}
	\item From Protocols~A/B, extract $\chi_{xx}(0)-\chi_{zz}(0)=w_{\parallel}\chi_{N}$; this reads off the pocket weight directly.
	\item Verify the trace bound $\sum\chi_{\mu\mu}(0)=2\chi_{N}$.
	\item Apply pressure or composition tuning that shifts $w_{\parallel}$; track $\chi_{zz}(0)/\chi_{N}$ along the one-parameter family Eq.~\eqref{eq:a2cr3as3-par}.
	\item Agreement of the observed trajectory with Eq.~\eqref{eq:a2cr3as3-pred} tests the band-resolved SOC-texture hypothesis of Sec.~\ref{sec:multiband-A2Cr3As3}. Disagreement (as in K$_{2}$Cr$_{3}$As$_{3}$, Sec.~\ref{sec:K2Cr3As3}) selects a different mechanism---most simply, a common $\mathbf{d}$-vector across all bands.
\end{enumerate}
In materials with significant inter-band pairing, deviations from Eq.~\eqref{eq:multiband-id} must be interpreted through a multi-orbital extension; the trace inequality Eq.~\eqref{eq:multiband-bound} remains valid regardless.
```

## §12 K₂Cr₃As₃ (trimmed)

```latex
\section{Worked example: K$_{2}$Cr$_{3}$As$_{3}$}
\label{sec:K2Cr3As3}

We walk through the protocols of Sec.~\ref{sec:protocols} using the $^{75}$As Knight-shift and $1/T_{1}$ data of Yang \emph{et al.}~\cite{Triplet2021} on single-crystal K$_{2}$Cr$_{3}$As$_{3}$. Three findings follow: (a) the observed ellipsoid sits at the oblate-axial vertex $(0,0,1)$ of the simplex; (b) the band-resolved SOC-texture prediction Eq.~\eqref{eq:a2cr3as3-pred} disagrees with the observation by $\sim 0.5$ in normalized Knight-shift units, selecting a common-$\mathbf{d}$-vector mechanism within the orbital-diagonal baseline; (c) the observed suppression of $1/T_{1}\parallel\hat c$ cannot come from the $\mathbf{q}=0$ spin-FGT budget and diagnoses finite-$\mathbf{q}$ FM spin-fluctuation gap formation.

\subsection{Inputs and direct diagnostic}
\label{sec:K2Cr3As3-inputs}

Reference~\cite{Triplet2021} reports the spin part $K_{s}=K-K_{\rm orb}$ of the $^{75}$As Knight shift at the As2 site after a standard Korringa separation of the orbital contribution ($K_{\rm orb}^{c}=0.27\%$, $K_{\rm orb}^{\perp c}=0.09\%$). Below $T_{c}$, Figs.~5 and 6 of Ref.~\cite{Triplet2021} establish
\begin{equation}
	\frac{K_{s}^{\perp c}(T\to 0)}{K_{s}^{\perp c}(T_{c}^{+})}=1\pm\epsilon_{ab},\qquad \frac{K_{s}^{c}(T\to 0)}{K_{s}^{c}(T_{c}^{+})}=0\pm\epsilon_{c},
	\label{eq:K2Cr3As3-raw}
\end{equation}
with $\epsilon_{ab},\epsilon_{c}\ll 1$. The sixfold in-plane rotational symmetry of the Knight shift reported in Fig.~2C of Ref.~\cite{Triplet2021} forces the \emph{measured} $K_{\mu\nu}(T)$ to be axially symmetric about $\hat c$ with principal axes along the crystallographic $(a,b,c)$, independent of the microscopic hyperfine structure. The reduction from $K_{\mu\nu}$ to projection eigenvalues proceeds component by component:
\begin{equation}
	\boxed{\;(\pi_{a},\pi_{b},\pi_{c})^{\rm obs}=(0\pm\epsilon_{ab},\,0\pm\epsilon_{ab},\,1\pm\epsilon_{c}).\;}
	\label{eq:K2Cr3As3-pi}
\end{equation}
The observed point sits at the oblate-axial vertex $(0,0,1)$ of Fig.~\ref{fig:simplex} within experimental uncertainty, and $\sum\pi_{i}=1\pm O(\epsilon)$ saturates the universal constraint Eq.~\eqref{eq:trace-from-ellipsoid}. Reading against Table~\ref{tab:ellipsoids}, Eq.~\eqref{eq:K2Cr3As3-pi} is the signature of an \emph{OSP unitary spin-triplet with $\mathbf{d}\parallel\hat c$}, or equivalently a quasi-1D SOC locking vector $\hat n\parallel\hat c$ on every pocket. This reproduces---via the ellipsoid diagnostic of Protocol~B, without invoking an $\mathbf{H}$-$T$ phase diagram---the principal conclusion of Ref.~\cite{Triplet2021}.

\subsection{Tension with the band-resolved SOC-texture prediction}
\label{sec:K2Cr3As3-bandtension}

The multi-band structural prediction Eq.~\eqref{eq:a2cr3as3-pred} assumes quasi-1D SOC along $\hat c$ on the $\alpha,\beta$ bands and approximately isotropic Rashba SOC on the 3D $\gamma$ band. Reference~\cite{Triplet2021} quotes a DFT value $w_{\gamma}\approx 0.75$ for K$_{2}$Cr$_{3}$As$_{3}$, i.e., $w_{\parallel}=1-w_{\gamma}\approx 0.25$. Substituting,
\begin{equation}
	(\pi_{a},\pi_{b},\pi_{c})^{\rm SOC-texture}=\Big(\tfrac{w_{\gamma}}{3},\tfrac{w_{\gamma}}{3},\,w_{\parallel}+\tfrac{w_{\gamma}}{3}\Big)\approx(0.25,\,0.25,\,0.50),
	\label{eq:K2Cr3As3-pred-SOC}
\end{equation}
a triaxial point at the midpoint of the median from the barycenter to the $\hat c$ vertex. The discrepancy with Eq.~\eqref{eq:K2Cr3As3-pi} is $\sim 0.5$ in normalized Knight-shift units, far beyond plausible experimental uncertainty. Allowing $w_{\gamma}$ to vary by a generous $\pm 33\%$ (to $w_{\gamma}=0.5$) still gives $(0.17,0.17,0.67)$, off by $\sim 0.33$; the tension is robust to DFT uncertainty.

Two mechanisms could produce the observed $\hat n\parallel\hat c$ rigidly on every band:
\begin{itemize}
	\item[(a)] \emph{$\mathbf{d}$-vector driven}: $\hat d_{\mathbf{k}}\parallel\hat c$ on all bands via the zero-SOC unitary-triplet identity Eq.~\eqref{eq:strong-triplet}.
	\item[(b)] \emph{SOC driven}: $\hat g_{\mathbf{k}}\parallel\hat c$ on all bands, including the 3D $\gamma$ band, via Eq.~\eqref{eq:strongSOCid}.
\end{itemize}
The Knight-shift ellipsoid alone does not distinguish (a) from (b). DFT calculations~\cite{Jiang15,Wu15}, however, indicate an approximately isotropic Rashba SOC on the $\gamma$ band, which contradicts (b); the tension captured in Eq.~\eqref{eq:K2Cr3As3-pred-SOC} makes this contradiction quantitative. Within the orbital-diagonal baseline of Sec.~\ref{sec:multiband}, mechanism (a) is the simplest remaining possibility, and $\hat d=\hat c$ rigidly on all pockets yields Eq.~\eqref{eq:K2Cr3As3-pi} exactly. This is consistent with the symmetry analysis of Ref.~\cite{Triplet2021} (Table~1 there): the $E'$ states $(p_{x}\pm ip_{y})\hat z$ have $\hat d\parallel\hat c$ on all bands.

\subsection{$1/T_{1}$ cross-check: finite-$\mathbf{q}$ fingerprint}
\label{sec:K2Cr3As3-T1}

Reference~\cite{Triplet2021} reports a sharp drop of $1/T_{1}$ below $T_{c}$ for both $\mathbf{H}\parallel\hat c$ and $\mathbf{H}\perp\hat c$, with no Hebel--Slichter peak. Applying the spin-FGT budget Eq.~\eqref{eq:T1-bound} to Eq.~\eqref{eq:K2Cr3As3-pi},
\begin{align}
	\mathbf{H}\parallel\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{a}+\pi_{b})\chi_{N}\approx 0,\\
	\mathbf{H}\perp\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{b}+\pi_{c})\chi_{N}\approx\chi_{N}.
	\label{eq:T1-K2Cr3As3}
\end{align}
The first line states that \emph{no} $\mathbf{q}=0$ spectral weight is available to suppress $1/T_{1}\parallel\hat c$. The observed drop in that orientation therefore exceeds the RHS of Eq.~\eqref{eq:T1-bound} and, by Protocol~D, is an unambiguous fingerprint of finite-$\mathbf{q}$ dominance. The natural candidate is the FM spin fluctuations identified in Ref.~\cite{Triplet2021} through the Curie-Weiss enhancement of $1/T_{1}T$ at $T>T_{c}$: they gap out below $T_{c}$ but are not constrained by the $\mathbf{q}=0$ budget. The absence of a Hebel--Slichter peak is a separate signature of the nodal $p$-wave gap structure, consistent with the $E'$ interpretation.

\subsection{Verdict and caveats}
\label{sec:K2Cr3As3-verdict}

Three pieces of evidence from Ref.~\cite{Triplet2021} are organized under the framework:
\begin{enumerate}
	\item Knight-shift ellipsoid at the $\hat c$ vertex of Fig.~\ref{fig:simplex}, saturating the trace bound.
	\item Band-resolved SOC-texture prediction Eq.~\eqref{eq:a2cr3as3-pred} with $w_{\gamma}=0.75$ off by $\sim 0.5$ in Knight-shift units; within the orbital-diagonal baseline, the data favor a \emph{rigid common $\mathbf{d}\parallel\hat c$ on all three bands}.
	\item Suppression of $1/T_{1}\parallel\hat c$ cannot come from $\mathbf{q}=0$ budget; diagnosed as finite-$\mathbf{q}$ FM spin-fluctuation gap formation.
\end{enumerate}
We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\mathbf{d}$-vector interpretation over the independent-pocket SOC-texture baseline. A definitive microscopic selection in the presence of strong inter-band pairing requires a multi-orbital BdG analysis---the Plancherel identity Eq.~\eqref{eq:general-sum-rule} survives that extension unchanged; only the specific anisotropic identity Eq.~\eqref{eq:multiband-id} needs refinement.

A targeted follow-up is an As1-vs-As2 site-resolved test (Protocol~E): under the common-$\mathbf{d}$-vector interpretation, the normalized projections must agree at the $\lesssim 5\%$ level. A systematic discrepancy at the $10$--$20\%$ level would signal inter-band parity mixing or a non-unitary triplet component; a discrepancy $\gtrsim 50\%$ would indicate failure of the single-band unitary BdG framework and require the multi-orbital extension noted above.
```

## §13 Summary

```latex
\section{Summary}
\label{sec:summary}

The Bogoliubov transformation's unitarity encodes a Plancherel identity Eq.~\eqref{eq:general-sum-rule} from which the spin-sector sum rule of Ref.~\cite{pang2026} is one specialization. Part~I developed the hierarchy of $T=0$ NMR-relevant consequences: the trace bound $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ on a 3D isotropic FS (Sec.~\ref{sec:isoT0}); the FS-shape-independent strong-locking anisotropic identity $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ (Sec.~\ref{sec:anisoT0}); the closed-form interpolation $F_{s}(\lambda)$ at arbitrary SOC, validated to $10^{-3}$ against existing numerics (Sec.~\ref{sec:intermediate}); its strong-locking finite-field extension $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]$ with quadratic stability of the zero-field ellipsoid (Sec.~\ref{sec:finiteH}); the spin-FGT sum rule tying Knight shift to integrated pair-breaking spectral weight (Sec.~\ref{sec:spinFGT}); and the multi-band decomposition with a structural prediction for the A$_{2}$Cr$_{3}$As$_{3}$ family (Sec.~\ref{sec:multiband}).

Part~II turned these identities into an experimental manual. Section~\ref{sec:ellipsoid} stated the Knight-shift ellipsoid theorem and the two-dimensional simplex of pairing classes, with a one-to-one correspondence between ellipsoid geometry and locking-vector texture (vertices=OSP/quasi-1D, edge-midpoints=ESP/2D Rashba, barycenter=singlet strong SOC). Section~\ref{sec:protocols} collected six protocols of increasing sophistication: trace bound (A), full-ellipsoid diagnostic (B), finite-field SOC-texture spectroscopy (C), $1/T_{1}$ cross-check (D), site-resolved consistency (E), and pocket decomposition (F). The number of independent rotation angles required is set by crystal symmetry: two for uniaxial, three for orthorhombic, six for triclinic. Regimes outside strong locking, most notably the opening of a Bogoliubov Fermi surface, lie outside the closed-form reach of the framework and are flagged as such.

Section~\ref{sec:K2Cr3As3} walked the protocols through the $^{75}$As data of Yang \emph{et al.}~\cite{Triplet2021} on K$_{2}$Cr$_{3}$As$_{3}$. The observed $(\pi_{a},\pi_{b},\pi_{c})=(0,0,1)$ sits at the oblate-axial $\hat c$ vertex of Fig.~\ref{fig:simplex} and saturates the trace bound. Combined with the band-resolved DOS fractions reported there, the decoupled-pocket structural prediction of Sec.~\ref{sec:multiband-A2Cr3As3} misses the observed vertex by $\sim 0.5$ in normalized Knight-shift units; within the orbital-diagonal baseline, the data favor a rigid common $\mathbf{d}\parallel\hat c$ on all three bands over the independent-pocket SOC-texture mechanism. The observed suppression of $1/T_{1}\parallel\hat c$ cannot originate from the $\mathbf{q}=0$ spin-FGT budget and is a direct fingerprint of finite-$\mathbf{q}$ FM spin-fluctuation gap formation, consistent with the Curie-Weiss enhancement of $1/T_{1}T$ above $T_{c}$.

The framework unifies Knight shift and $1/T_{1}$ under a single geometric principle: total matrix-element weight is the trace-squared of the probe operator in the single-particle basis. Combined with band-structure input, it constrains different spin-triplet mechanisms at the same observed pairing symmetry. It invites systematic tests across the A$_{2}$Cr$_{3}$As$_{3}$ family under pressure and composition tuning and across different NMR-active sites within a single compound. A definitive microscopic selection in the presence of strong inter-band pairing requires a multi-orbital extension of the specific anisotropic identity; the underlying Plancherel identity survives that extension unchanged.

\bibliographystyle{apsrev4-2}
\bibliography{mag-soc}

\end{document}
```

That completes v8. Summary of what changed from v7:

- **Two-part logical structure** enforced through the bridge paragraph before §10 and explicit "Part~I/Part~II" language in intro, abstract, and summary. No `\part{}` command used.
- **All six experimental protocols** pulled out of individual theory sections and consolidated in §11, with a summary table (`tab:protocols`) up front showing what each protocol measures, output, assumptions, and failure mode.
- **Ellipsoid theorem and simplex figure** moved entirely to Part II (§10), with the pairing-class catalogue and oblate/prolate/triaxial discussion.
- **Multi-band section** (§9) now sits in Part~I with just the structural prediction; the A$_{2}$Cr$_{3}$As$_{3}$-specific pocket-decomposition protocol went to §11 as Protocol F.
- **K$_{2}$Cr$_{3}$As$_{3}$ section trimmed** from ~seven subsections to four: inputs+diagnostic combined; tension with SOC-texture kept but compressed; site-resolved section folded into the verdict as a follow-up recommendation; interband-pairing caveat merged into verdict. Duplication between former §11.3 and §11.6 removed.
- **Abstract rewritten** to reflect the two-part organization.

If you want any section rebalanced (e.g., more detail restored to K$_2$Cr$_3$As$_3$, or the protocols table expanded), let me know.

---
## 🧑‍💻 User

Here is the revised version. Please go through it.

---
## 🤖 Assistant

I went through v14 carefully. The new logical ordering and the parity-mixed insertion are a real improvement — the paper now reads as a single derivation chain rather than a catalogue. The K₂Cr₃As₃ analysis in particular is much cleaner because each subsection is labeled with the protocol it invokes. Below are the issues I found, ordered by priority.

## High priority

**1. Wide equations will overflow in twocolumn.** Several inline equations fit in onecolumn but will break out of the column box in twocolumn. Specifically:

- Eq.~\eqref{eq:chi-FSaverage} packs two equations on one line via `\quad`. In twocolumn this overflows. Split:
```latex
\begin{align}
\chi_{\mu\nu}(0) &= \tfrac{\chi_{N}}{2}\big\langle[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\tilde J(\lambda_{\mathbf{k}})\big\rangle_{\rm FS}, \label{eq:chi-FSaverage}\\
\tilde J(\lambda) &= \int_{-\infty}^{\infty}\!d\xi\,\mathcal{F}(\xi,\lambda\Delta,\Delta). \label{eq:Jdef}
\end{align}
```

- Eq.~\eqref{eq:spinFGT} is likely to overflow. Wrap it in `\begin{widetext}...\end{widetext}` or break the chain:
```latex
\begin{widetext}
\begin{equation}
\boxed{\;\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\big[\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)-\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega)\big]=\chi_{N}-\chi_{\mu\mu}(0)=\chi_{N}\pi_{\mu}.\;}
\label{eq:spinFGT}
\end{equation}
\end{widetext}
```

- Eq.~\eqref{eq:K-intermediate} will likely overflow; same fix.
- Eq.~\eqref{eq:Khf-trace} packs two statements with `\qquad`; split into two lines.

I would run one test compile in twocolumn and check every boxed equation — the boxes make overflows visually obvious.

**2. Appendix A figure is not using a float.** The manual counter hack will almost certainly misbehave (wrong number if any figure precedes it, no proper float placement, broken hyperref anchor for `fig:fig3-t0-validation` which is referenced from §8):
```latex
\begin{center}
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
\end{center}
\refstepcounter{figure}\label{fig:fig3-t0-validation}
\noindent\textbf{FIG. \thefigure.} ...
```
Replace with a proper figure environment:
```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
```

**3. Preamble has `\usepackage{bm}` twice** (lines 10 and 14). Harmless but should be cleaned up. Also `lipsum`, `cancel`, `soul`, `subfigure` (deprecated) appear unused; drop them.

## Medium priority

**4. Small ambiguity in the parity-mixed claim, §7.** The closing sentence of Sec.~\ref{sec:paritymix-consequences} reads
> Once $\Delta_{\perp}$ is sizable, one helicity sheet is weakly paired or gapless, or inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem.

The three conditions look like a sequence rather than alternatives. Inserting "or" clarifies:
> Once $\Delta_{\perp}$ is sizable, \emph{or} one helicity sheet is weakly paired or gapless, \emph{or} inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem.

**5. Physical claim to sharpen in §7.** Eq.~\eqref{eq:paritymix-chiT} is correct and the argument that parity mixing is invisible at $T=0$ but shows up in the finite-$T$ recovery through two distinct Yosida factors $Y_\pm(T; \Delta_\pm)$ is a nice new result. Worth adding a one-line experimental corollary at the end of §7, since this is effectively a new diagnostic: a two-scale recovery of $K(T)$ below $T_c$ with the same $T=0$ ellipsoid as a pure locking texture is the signature of a helicity-diagonal parity-mixed state. That's a genuine prediction, and stating it explicitly strengthens the section's payoff.

**6. Scope of Eq.~\eqref{eq:multiband-bound} slightly understated.** The closing sentence of §11.2 says the trace bound "should then be treated as part of the decoupled-pocket baseline unless it is rederived in the extended model." Strictly, the pointwise Plancherel bound $\sum|M_{pp,O}|^2\le\mathrm{Tr}_s(O^2)$ plus $\langle\cos^2\theta\rangle = 1/3$ on an isotropic FS gives $\chi_O(0)\le (2/3)\chi_O^N$ regardless of orbital-diagonal pairing; additivity of $\chi_N$ across pockets is pure Kubo linearity. So Eq.~\eqref{eq:multiband-bound} survives inter-band pairing on a 3D isotropic FS. What requires orbital-diagonality is the \emph{anisotropic} identity Eq.~\eqref{eq:multiband-id}. Consider:
> Equation~\eqref{eq:multiband-id} is exact for orbital-diagonal pairing and is a baseline otherwise; the trace inequality Eq.~\eqref{eq:multiband-bound}, in contrast, follows directly from the Plancherel identity and the isotropic-FS geometry and therefore survives inter-band pairing.

**7. Intro word choice.** "We elevate that relation to one member of a broader Plancherel family" — "elevate ... to one member" is awkward. Consider "We recognize that relation as one specialization of a broader Plancherel family" or "we show that relation is one member of a broader Plancherel family."

## Low priority / style

**8. "Short" section titles in TOC.** The form `\section[Exact Identity]{Exact identity: generalized Bogoliubov sum rule}` works. One thing to check: in revtex4-2 twocolumn, the TOC may not auto-typeset nicely. Worth eyeballing the generated TOC once.

**9. Trailing subsection in §9 mentions Protocol C**:
> Protocol~C below is built precisely around this regime separation...

This is a good forward reference. Same pattern is used in §8 ("deployed as Protocol~B in Sec.~\ref{sec:protocols}"). These forward references are useful but tie the theory sections to the protocol labels. If protocol labels ever shift during revision, these will need to be updated — a find-and-replace point during proofing.

**10. Table~\ref{tab:sat} uses `table[b]`** — single-column float pinned to bottom. Since the table is narrow this is fine, but in twocolumn it may float away from its reference. Consider `table[tbp]`.

**11. Ref.~\cite{Triplet2021}'s Table 1 citation** in §14.2: "the $E'$ states $(p_x \pm ip_y)\hat z$ have $\hat d \parallel \hat c$ on all bands." This is a clean, specific citation. Good.

## Physics spot-check (no changes needed)

- Eq.~\eqref{eq:paritymix-helicity-gap} with $\Delta_\pm = \psi \pm d_\parallel$ checks out: projecting $\Delta(\mathbf{k}) = i[\psi\sigma_0 + \mathbf{d}\cdot\sigma]\sigma_y$ onto helicity eigenstates of $\hat g\cdot\sigma$ gives additive contributions on the two sheets with opposite signs for $d_\parallel$.
- Eq.~\eqref{eq:paritymix-chiT} with $\chi/\chi_N = \delta - \Pi + \sum_\lambda w_\lambda \langle Y_\lambda \hat n_\mu \hat n_\nu\rangle_\lambda$ reduces correctly at $T\to 0$ (fully gapped) to Eq.~\eqref{eq:paritymix-T0}, and at $T\to T_c$ to $\delta_{\mu\nu}$ (normal state) since $Y_\lambda(T_c)=1$ makes the last term equal to $+\Pi_{\mu\nu}$.
- K₂Cr₃As₃ SOC-texture prediction: with $w_\gamma = 0.75$, $(\pi_a, \pi_b, \pi_c) = (0.25, 0.25, 0.50)$ — matches Eq.~\eqref{eq:K2Cr3As3-pred-SOC} and $\sum = 1$.

## Summary

The manuscript is in good shape. The three issues that would actually break the PDF or degrade the experience are the twocolumn overflow of the wider equations, the appendix figure hack, and the duplicate `\usepackage{bm}`. Fix those, tighten the closing sentence of §7, and consider adding the two-scale-recovery diagnostic as a one-line experimental corollary after Eq.~\eqref{eq:paritymix-T0}.

Want me to produce a patched v15 with just these fixes, or would you prefer to apply them yourself and keep the diff small?

---
## 🧑‍💻 User

Pleas give me such patches.

---
## 🤖 Assistant

Here are the patches as drop-in replacements. Apply in order; each is self-contained.

## Patch 1 — Preamble cleanup

Replace the package block near the top with:

```latex
\documentclass[prb,aps,twocolumn,superscriptaddress]{revtex4-2}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage{amsmath}
\usepackage{color}
\usepackage{bm}
\usepackage{amssymb}
\usepackage{epsfig}
\usepackage{multirow}
\usepackage{amsbsy}
\usepackage{array}
\usepackage{diagbox}
\usepackage{extarrows}
\usepackage{graphicx}
\usepackage{appendix}
\usepackage{txfonts}
\usepackage{tablefootnote}
\graphicspath{{figures/}}
\allowdisplaybreaks[4]
\newcommand{\tabincell}[2]{\begin{tabular}{@{}#1@{}}#2\end{tabular}}

\usepackage[colorlinks=true,linkcolor=blue,citecolor=blue,urlcolor=blue,bookmarks=false]{hyperref}
```

Removed: duplicate `bm`, and unused `subfigure`, `lipsum`, `cancel`, `soul`.

## Patch 2 — Intro word choice

In §\ref{sec:intro}, replace the sentence

```latex
In this paper we elevate that relation to one member of a broader Plancherel family and organize the manuscript around its consequences.
```

with

```latex
In this paper we show that relation is one member of a broader Plancherel family and organize the manuscript around its consequences.
```

## Patch 3 — Eq.~\eqref{eq:chi-FSaverage} split

In §\ref{sec:intermediate}, replace

```latex
\begin{equation}
    \chi_{\mu\nu}(0)=\tfrac{\chi_{N}}{2}\langle[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\tilde J(\lambda_{\mathbf{k}})\rangle_{\rm FS},\quad \tilde J(\lambda)=\int_{-\infty}^{\infty}d\xi\,\mathcal{F}(\xi,\lambda\Delta,\Delta),
    \label{eq:chi-FSaverage}
\end{equation}
```

with

```latex
\begin{align}
    \chi_{\mu\nu}(0) &= \tfrac{\chi_{N}}{2}\big\langle[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\tilde J(\lambda_{\mathbf{k}})\big\rangle_{\rm FS}, \label{eq:chi-FSaverage}\\
    \tilde J(\lambda) &= \int_{-\infty}^{\infty}\!d\xi\,\mathcal{F}(\xi,\lambda\Delta,\Delta), \label{eq:Jdef}
\end{align}
```

## Patch 4 — Eq.~\eqref{eq:spinFGT} widetext

In §\ref{sec:spinFGT}, replace

```latex
\begin{equation}
    \boxed{\;\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\big[\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)-\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega)\big]=\chi_{N}-\chi_{\mu\mu}(0)=\chi_{N}\pi_{\mu},\;}
    \label{eq:spinFGT}
\end{equation}
```

with

```latex
\begin{widetext}
\begin{equation}
    \boxed{\;\frac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}\,\big[\mathrm{Im}\,\chi_{\mu\mu}^{N}(\omega)-\mathrm{Im}\,\chi_{\mu\mu}^{SC}(\omega)\big]=\chi_{N}-\chi_{\mu\mu}(0)=\chi_{N}\pi_{\mu},\;}
    \label{eq:spinFGT}
\end{equation}
\end{widetext}
```

## Patch 5 — Eq.~\eqref{eq:K-intermediate} widetext

In §\ref{sec:ellipsoid}, subsection on intermediate-SOC ellipsoid contraction, replace

```latex
\begin{equation}
    \frac{K(\hat{\mathbf{H}},0)}{K_{N}}=\big\langle F_{s}(\lambda_{\mathbf{k}})\big[1-(\hat{\mathbf{H}}\cdot\hat n_{\mathbf{k}})^{2}\big]\big\rangle_{\rm FS}
    \equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
    \label{eq:K-intermediate}
\end{equation}
```

with

```latex
\begin{widetext}
\begin{equation}
    \frac{K(\hat{\mathbf{H}},0)}{K_{N}}=\big\langle F_{s}(\lambda_{\mathbf{k}})\big[1-(\hat{\mathbf{H}}\cdot\hat n_{\mathbf{k}})^{2}\big]\big\rangle_{\rm FS}
    \equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}}.
    \label{eq:K-intermediate}
\end{equation}
\end{widetext}
```

(also changed the trailing comma to a period, since the chain ends there.)

## Patch 6 — Eq.~\eqref{eq:Khf-trace} split

In §\ref{sec:ellipsoid-hf}, replace

```latex
\begin{equation}
    \sum_{i}\frac{K_{i}(0)}{K_{i}(T_{c}^{+})}=2,\qquad 0\le\frac{K_{i}(0)}{K_{i}(T_{c}^{+})}=1-\pi_{i}\le 1.
    \label{eq:Khf-trace}
\end{equation}
```

with

```latex
\begin{align}
    \sum_{i}\frac{K_{i}(0)}{K_{i}(T_{c}^{+})} &= 2, \label{eq:Khf-trace}\\
    0\le\frac{K_{i}(0)}{K_{i}(T_{c}^{+})} &= 1-\pi_{i}\le 1. \label{eq:Khf-bound}
\end{align}
```

## Patch 7 — §\ref{sec:paritymix-consequences} closing clarification and experimental corollary

Replace the final paragraph of §\ref{sec:paritymix-consequences} (from "A fully gapped helicity-diagonal parity mixture..." through the end of the section) with:

```latex
A fully gapped helicity-diagonal parity mixture therefore does \emph{not} generate a new $T=0$ simplex point: it shares the same projector geometry as the corresponding locking texture. What changes is the finite-$T$ recovery, because the two helicity sheets generally carry different gaps $\Delta_{\pm}$. Taking the trace of Eq.~\eqref{eq:paritymix-chiT} gives
\begin{equation}
    \frac{\mathrm{Tr}\,\chi(T)}{\chi_{N}}
    =
    2+\sum_{\lambda=\pm}w_{\lambda}\langle Y_{\lambda}(\mathbf{k},T)\rangle_{\lambda},
    \label{eq:paritymix-trace}
\end{equation}
using $\mathrm{Tr}\,\Pi=1$. Unequal $\Delta_{\pm}$ therefore produce a broadened or two-scale return of the Knight shift with temperature even when the $T=0$ ellipsoid is unchanged. This yields a concrete experimental corollary: a two-scale recovery of $K_{\mu\nu}(T)$ below $T_{c}$ whose $T\to 0$ limit coincides with a pure-locking simplex point is a positive signature of a helicity-diagonal parity-mixed state. A single-gap Yosida recovery onto the same $T=0$ ellipsoid is consistent with the pure locking texture. This upgrades the ellipsoid from a vertex/edge classifier to a finite-$T$ discriminator between pure and parity-mixed pairing, at no additional experimental cost.

Once $\Delta_{\perp}$ is sizable, \emph{or} one helicity sheet is weakly paired or gapless, \emph{or} inter-band pairing dominates, Eq.~\eqref{eq:paritymix-T0} should be treated as a baseline rather than a theorem.
```

## Patch 8 — §\ref{sec:multiband} scope clarification

In §\ref{sec:multiband} (subsection "Scope: inter-band pairing as deviation from baseline"), replace the first two sentences with:

```latex
Equation~\eqref{eq:multiband-id} is exact for orbital-diagonal pairing and is a baseline otherwise: deviations diagnose the inter-band structure. The trace inequality Eq.~\eqref{eq:multiband-bound}, in contrast, follows directly from the pointwise Plancherel bound $\sum|M_{pp,O}|^{2}\le\mathrm{Tr}_{s}(O^{2})$ and the isotropic-FS geometric factor $\langle\cos^{2}\theta\rangle=1/3$; it therefore survives inter-band pairing on a 3D isotropic FS. The Plancherel identity Eq.~\eqref{eq:general-sum-rule} itself is independent of the orbital-diagonal assumption. A dedicated multi-orbital derivation is required, however, before importing the anisotropic simplex interpretation of Sec.~\ref{sec:ellipsoid}, or the normalized site/pocket bounds used later, to genuine inter-band pairing.
```

Then in Protocol F (§\ref{sec:protocolF}), replace the closing sentence

```latex
In materials with significant inter-band pairing, deviations from Eq.~\eqref{eq:multiband-id} must be interpreted through a multi-orbital extension; Eq.~\eqref{eq:multiband-bound} should then be treated as part of the decoupled-pocket baseline unless it is rederived in the extended model.
```

with

```latex
In materials with significant inter-band pairing, deviations from Eq.~\eqref{eq:multiband-id} must be interpreted through a multi-orbital extension; the isotropic trace inequality Eq.~\eqref{eq:multiband-bound} survives that extension, but the anisotropic decomposition does not.
```

## Patch 9 — Appendix A figure

Replace the figure block in Appendix~\ref{app:intermediate-support},

```latex
\begin{center}
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
\end{center}
\refstepcounter{figure}\label{fig:fig3-t0-validation}
\noindent\textbf{FIG. \thefigure.} Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.
\par
```

with

```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
```

## Patch 10 — Float placement of Table~\ref{tab:sat}

Minor: change the specifier from `[b]` to `[tb]` to give revtex more freedom in twocolumn:

```latex
\begin{table}[tb]
    \caption{Saturation of the trace bound $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$. Components in units of $\chi_{N}$.}
    \label{tab:sat}
```

## Suggested compile order for sanity

After applying, compile once and scan for:

1. Column overflow on boxed equations (any still sticking out? move to `widetext`).
2. TOC rendering — revtex4-2 twocolumn TOC can look cramped; if so, use short titles consistently in `\section[...]{...}`.
3. The `\ref{fig:fig3-t0-validation}` reference in §\ref{sec:intermediate-closed} now resolves through a normal float; confirm the number.
4. All `\ref{eq:...}` to the split equations (Patches 3, 6) still resolve to the intended label — I kept the original label on the first line in each case, so references in the body text do not need updating.

None of these patches touch physics content except Patch 7, which adds the two-scale-recovery diagnostic as a new experimental corollary. If you'd rather keep §7 minimal and defer that corollary to the summary or to Protocol B, let me know and I'll rework it.

---
## 🧑‍💻 User

Here is the revised version. How about adding a summary table for useful equations or inequality?

---
## 🤖 Assistant

Yes — a "key results" reference table is exactly the kind of thing a manual paper benefits from. It serves two functions: (a) the reader can locate the right inequality without paging back, and (b) reviewers can verify at a glance that the framework's main claims are clearly delineated.

I would place it at the end of Sec.~\ref{sec:multiband}, right before the bridge paragraph that hands off to the experimental sections. That position makes it the natural divider between the theoretical and experimental halves of the paper: everything above it is derivation, everything below it uses the entries as building blocks.

Before I write it, also: there's a stray duplicate caption in Appendix~\ref{app:intermediate-support} that I should flag — after the figure environment you have an orphan `\noindent\textbf{FIG. \thefigure.}` block that duplicates the figure caption. It should just be deleted. Patch at the end.

## Patch 11 — Key results summary table

Insert just before the closing bridge paragraph of §\ref{sec:multiband} (i.e., between the end of §\ref{sec:multiband-A2Cr3As3} and the "The preceding theory sections produced..." paragraph). The table:

```latex
\subsection{Summary of key identities and inequalities}
\label{sec:keyresults}

Table~\ref{tab:keyresults} collects the central identities and inequalities of the theoretical part for reference in the experimental sections that follow. Each entry is keyed to the protocol that deploys it.

\begin{table*}[tb]
    \caption{Key identities and inequalities. The right column points to where the result is deployed in the experimental sections. All identities assume the single-band unitary BdG framework of Sec.~\ref{sec:setup}.}
    \label{tab:keyresults}
    \renewcommand\arraystretch{1.5}
    \setlength{\tabcolsep}{0.7ex}
    \begin{tabular}{l|l|l|l|l}
        \hline\hline
        \# & Result & Statement & Domain of validity & Used in\\
        \hline
        1 & Plancherel identity & $\sum_{s_{1}s_{2}}\!\big[|M^{s_{1}s_{2}}_{ph,O}|^{2}+|M^{s_{1}s_{2}}_{pp,O}|^{2}\big]=\mathrm{Tr}_{s}(O^{2})$ & any Hermitian $O$, any $\mathbf{k}$ & all subsequent results\\
        2 & Universal $T=0$ bound & $\chi_{O}(0)\le\tfrac{2}{3}\,\chi_{O}^{N}$ & 3D isotropic FS, any $O$ & Eq.~\eqref{eq:universal-23}\\
        3 & Isotropic trace bound & $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ & 3D isotropic FS & Protocol A\\
        4 & Site-resolved bound & $\mathrm{Tr}\,K^{(\mathbf{R})}(0)/\mathrm{Tr}\,K^{(\mathbf{R})}(T_{c})\le 2/3$ & any nucleus $\mathbf{R}$, isotropic FS & Protocol E\\
        5 & Strong-locking identity & $\chi_{\mu\nu}(0)/\chi_{N}=\delta_{\mu\nu}-\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ & $|\mathbf{g}|/\Delta\to\infty$ or unitary triplet & Protocol B (ellipsoid)\\
        6 & Trace from ellipsoid & $\sum_{i}K_{i}(0)=2K_{N}$ & strong locking, any FS/SOC & Protocol B (simplex)\\
        7 & Helicity-diagonal $T=0$ & $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ & parity mixture with $\Delta_{\perp}=0$, fully gapped & Sec.~\ref{sec:K2Cr3As3-bandtension}\\
        8 & Intermediate-SOC, $s$-wave & $\chi_{\mu\nu}(0)/\chi_{N}=\langle F_{s}(\lambda_{\mathbf{k}})[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\rangle_{\rm FS}$ & $\mathbf{H}=0$, $s$-wave, any SOC & Protocol B (intermediate)\\
        9 & $F_{s}$ closed form & $F_{s}(\lambda)=1-\sinh^{-1}\!\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ & same as \#8 & SOC spectroscopy\\
        10 & Finite-$\mathbf{H}$ strong locking & $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]+O(\Delta^{2}/b_{\min}^{2})$ & $b_{\min}(\mathbf{H})\gg\Delta$ & Protocol C\\
        11 & Zero-field stability & $\Pi_{\mu\nu}(\mathbf{H})=\Pi_{\mu\nu}(0)+O(h^{2}/\lambda^{2})$ & $\mu_{B}H\ll|\mathbf{g}_{\mathbf{k}}|$ on FS & Protocol C (low field)\\
        12 & Spin FGT sum rule & $\tfrac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}[\mathrm{Im}\chi^{N}-\mathrm{Im}\chi^{SC}]=\chi_{N}\pi_{\mu}$ & strong locking, $\mathbf{q}=0$ & Protocol D\\
        13 & $1/T_{1}$ heuristic bound & $\int_{0}^{T_{c}}\!\frac{dT}{T}[(T_{1}^{N})^{-1}-(T_{1}^{SC})^{-1}]\lesssim\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\pi_{\mu}$ & $\mathbf{q}\approx 0$ dominant & Protocol D\\
        14 & Multiband decomposition & $\chi_{\mu\nu}(0)=\sum_{i}\chi_{N}^{(i)}[\delta_{\mu\nu}-\Pi^{(i)}_{\mu\nu}]$ & orbital-diagonal pairing & Protocol F\\
        15 & Multiband trace bound & $\mathrm{Tr}\,\chi(0)\le(2/3)\mathrm{Tr}\,\chi(T_{c})$ & 3D isotropic FS, any pairing & survives interband mixing\\
        \hline\hline
    \end{tabular}
\end{table*}
```

Entries are ordered as in the manuscript flow. Each row's "Domain of validity" column is the single most important piece of information a reader needs when reaching for the formula — it answers the question "may I use this here?" without rereading the section. The "Used in" column is the back-reference into the experimental side.

If you want to keep the table tighter, drop rows 2 and 7 (entry 2 is a generalization of entry 3, entry 7 follows from entry 5 in the helicity-diagonal limit). I would keep both because they are conceptually distinct claims used in different places.

## Patch 12 — Remove duplicate caption in Appendix A

In Appendix~\ref{app:intermediate-support}, the figure block is currently:

```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
\noindent\textbf{FIG. \thefigure.} Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.
\par
```

The block after `\end{figure}` (from `\noindent` through `\par`) is a leftover from the v14 manual-caption version. Delete it. The figure's own caption inside the float is correct and sufficient. Final form:

```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
```

## Two minor optional improvements I'd consider

**A. Cross-reference the summary table from §\ref{sec:protocols}.** After the opening paragraph of §\ref{sec:protocols}, before Table~\ref{tab:protocols}, add a sentence:
> The identities and inequalities invoked by each protocol are collected in Table~\ref{tab:keyresults}.

This closes the loop: a reader entering the manual side directly can find every formula they need.

**B. Optional: add a row 0 to Table~\ref{tab:keyresults}** with the locking-projector \emph{definition} itself, $\Pi_{\mu\nu}=\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$, $\mathrm{Tr}\,\Pi=1$ — since this object appears in 6 of the 15 entries and is the geometric thread of the paper, having it visible at the top of the table reinforces the reading order. Up to you.

Let me know if you'd like me to slim or expand the table — e.g., add a "Saturation condition" column (when is the inequality an equality?) which would be highly useful for the manual purpose but adds width.

---
## 🧑‍💻 User

Here is the revised version.

---
## 🤖 Assistant

I went through v15. The summary table reads well in its placement, and the major patches all landed correctly. There are five remaining issues to address, ordered by impact.

## High priority

**1. Both appendix figures use the manual `\refstepcounter` hack, not float environments.** This is the issue I flagged in v14 — Patch 9 in my earlier response fixed it for Appendix A, but the patch was reverted in v15. Both Appendix A and Appendix B now have the same problem:

```latex
\begin{center}
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
\end{center}
\refstepcounter{figure}\label{fig:fig3-t0-validation}
\noindent\textbf{FIG. \thefigure.} Cross-check of ...
```

This will produce three problems with revtex4-2 in twocolumn:

- the figure has no proper float placement, so it lands wherever in the column flow rather than being floated to top/bottom;
- it will not float across columns even if oversized;
- `\thefigure` may print the wrong number if any future float is added before it. (For two-column layouts revtex4-2 numbers floats in placement order, and a manual counter increment can desync from the auto-numbered figures.)

The proper fix is to use `figure*` (spans both columns) or `figure` (single column) environments:

For Appendix A:
```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
```

For Appendix B:
```latex
\begin{figure}[tb]
    \centering
    \begin{tikzpicture}[scale=0.9]
        ... (existing TikZ code) ...
    \end{tikzpicture}
    \caption{Schematic: $\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$ in the normal state (blue) and the SC state (red). Spectral weight of magnitude $\chi_{N}\pi_{\mu}$ is transferred from the static peak at $\omega\to 0$ into the pair-breaking continuum above $2\Delta_{\min}$, conserving the Kramers--Kronig integral Eq.~\eqref{eq:spinFGT}. The Van Vleck bump at the interband threshold is essentially unaffected by pairing at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$.}
    \label{fig:spinFGT-spectral}
\end{figure}
```

Note `\centering` not `\begin{center}` inside the float — the `center` environment adds extra vertical space.

## Medium priority

**2. `\end{widetext}` orphaned period issue around Eq.~\eqref{eq:K-intermediate}.** The current code is:

```latex
\begin{widetext}
\begin{equation}
    \frac{K(\hat{\mathbf{H}},0)}{K_{N}}= ... \equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}}.
    \label{eq:K-intermediate}
\end{equation}
\end{widetext}
with $S(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$ and ...
```

The "with" sentence starts a new paragraph after the widetext block, but the equation ends with a period. So the prose reads "...$\hat{\mathbf{H}}$. with $S(\lambda)$..." which is ungrammatical. Two options:

(a) change the equation's terminal period to a comma and keep the "with..." continuation. Cleanest:
```latex
    \equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
```

(b) keep the period and restart the next sentence with "Here" instead of "with":
```latex
Here $S(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$, and
```

I'd go with (a).

**3. Table~\ref{tab:keyresults} placement.** The table is currently inside `\subsection{Summary of key identities and inequalities}` inside §\ref{sec:multiband}, and is a `table*` so it spans both columns. That's the correct float type. The minor issue is that the subsection label `\label{sec:keyresults}` is in a subsection that is purely a wrapper for the table — it's three sentences of intro plus the table. Two readability suggestions:

(a) Promote it from a subsection of §\ref{sec:multiband} to a top-level section between §\ref{sec:multiband} and §\ref{sec:ellipsoid}. This makes its role as a "bridge between Part I and Part II" structurally explicit rather than buried as the last subsection of the multiband section. Title: `\section{Reference table of key identities}\label{sec:keyresults}`.

(b) Or, leave it as a subsection but move it to be a subsection of §\ref{sec:protocols} (after the protocols table) so the two summary tables sit together.

I think (a) is the better choice: the table serves the entire experimental manual that follows, not just multiband considerations.

## Low priority / style

**4. Quotation marks in Table~\ref{tab:protocols} caption.** Currently:
```latex
"3-axis $K$" means ... "rotation" means ...
```
Both `"..."` are straight (ASCII) quotes. In LaTeX these will render as `"..."` (two opening doubles in a row) rather than typographic quotes. Replace with `\`\`...''`:
```latex
``3-axis $K$'' means ... ``rotation'' means ...
```

**5. `floatfix` package option.** The new preamble has `floatfix` as a class option:
```latex
\documentclass[prb,aps,twocolumn,superscriptaddress,floatfix]{revtex4-2}
```
`floatfix` is a known revtex4-2 option that fixes some float placement issues but can also occasionally produce unexpected layouts with `table*` environments. If after applying patch 1 above you still see odd placement of either appendix figure or `tab:keyresults`, try removing `floatfix` and recompiling. It is usually safer to leave off unless specifically needed.

## Quick patch bundle

For convenience here are the smallest possible diffs as drop-in patches.

### Patch A: Appendix A figure

Replace
```latex
\begin{center}
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
\end{center}
\refstepcounter{figure}\label{fig:fig3-t0-validation}
\noindent\textbf{FIG. \thefigure.} Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.
\par
```
with
```latex
\begin{figure}[tb]
    \centering
    \includegraphics[width=\linewidth]{figures/fig3_t0_validation}
    \caption{Cross-check of Eq.~\eqref{eq:Fs} against the $T=0$ endpoints of the $s$-wave curves in Fig.~3 of Ref.~\cite{pang2026}. Solid line: Eq.~\eqref{eq:fig3-crosscheck}. Symbols: extracted intercepts. Lower panel: digitized minus theory.}
    \label{fig:fig3-t0-validation}
\end{figure}
```

### Patch B: Appendix B figure

Replace
```latex
\begin{center}
    \begin{tikzpicture}[scale=0.9]
        ... tikz code ...
    \end{tikzpicture}
\end{center}
\refstepcounter{figure}\label{fig:spinFGT-spectral}
\noindent\textbf{FIG. \thefigure.} Schematic: $\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$ ...
\par
```
with
```latex
\begin{figure}[tb]
    \centering
    \begin{tikzpicture}[scale=0.9]
        ... tikz code unchanged ...
    \end{tikzpicture}
    \caption{Schematic: $\mathrm{Im}\,\chi_{\mu\mu}(\omega)/\omega$ in the normal state (blue) and the SC state (red). Spectral weight of magnitude $\chi_{N}\pi_{\mu}$ is transferred from the static peak at $\omega\to 0$ into the pair-breaking continuum above $2\Delta_{\min}$, conserving the Kramers--Kronig integral Eq.~\eqref{eq:spinFGT}. The Van Vleck bump at the interband threshold is essentially unaffected by pairing at leading order in $\Delta/|\mathbf{g}_{\mathbf{k}}|$.}
    \label{fig:spinFGT-spectral}
\end{figure}
```

### Patch C: Eq.~\eqref{eq:K-intermediate} grammar

Change the last line of the equation from
```latex
\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}}.
```
to
```latex
\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
```
(period → comma, so the "with..." sentence flows).

### Patch D: Promote key-results subsection to a section

Currently:
```latex
\subsection{Summary of key identities and inequalities}
\label{sec:keyresults}

Table~\ref{tab:keyresults} collects ...
```
nested inside §\ref{sec:multiband}.

Move this entire block (intro paragraph + table) out of §\ref{sec:multiband} and place it as a top-level section between the end of §\ref{sec:multiband} and §\ref{sec:ellipsoid}, retitled:

```latex
\section{Reference table of key identities}
\label{sec:keyresults}

Before turning to the experimental manual we collect the central identities and inequalities derived above. Each entry in Table~\ref{tab:keyresults} is keyed to the protocol that deploys it in Sec.~\ref{sec:protocols}.

\begin{table*}[tb]
    ... existing table unchanged ...
\end{table*}
```

This also moves the existing bridge paragraph ("The preceding theory sections produced four kinds of input...") with the table — it should stay as the lead-in to §\ref{sec:ellipsoid} but does not need to move.

Actually on second reading, that bridge paragraph fits more naturally as the opening paragraph of §\ref{sec:ellipsoid} rather than tail-end of §\ref{sec:keyresults}. Consider moving it.

### Patch E: Smart quotes in tab:protocols caption

Change
```latex
"3-axis $K$" means Knight shift measured ... "rotation" means full angular scan ...
```
to
```latex
``3-axis $K$'' means Knight shift measured 

---
## 🧑‍💻 User

Here is the revised version.

---
## 🤖 Assistant

I read through v15 carefully. The structural plan is in good shape now — both appendix figures are proper float environments, the smart quotes are fixed in the protocols-table caption, and the duplicate `\usepackage{bm}` is gone. The remaining issues are small and would not block submission, but I'd recommend addressing them before circulating to coauthors or submitting to PRB.

## What's still worth fixing

**1. Eq.~\eqref{eq:K-intermediate} terminal period.** Still a period, not a comma — the `with...` sentence that follows reads as broken grammar:

```latex
\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}}.
\label{eq:K-intermediate}
...
\end{widetext}
with $S(\lambda)\equiv\langle F_{s}...
```

Either change the trailing period to a comma:
```latex
\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}},
```
or capitalize the continuation: change `with` to `Here`.

**2. Table~\ref{tab:keyresults} placement.** The key-results table is still a subsection inside §\ref{sec:multiband}. As I noted before, this table serves the entire experimental manual, not just the multiband material. Strong recommendation: promote it to its own top-level section between §\ref{sec:multiband} and §\ref{sec:ellipsoid}:

```latex
\section{Reference table of key identities}
\label{sec:keyresults}

Before turning to the experimental manual we collect the central identities and inequalities derived above. Each entry in Table~\ref{tab:keyresults} is keyed to the protocol that deploys it in Sec.~\ref{sec:protocols}.

\begin{table*}[tb]
    ... existing table unchanged ...
\end{table*}
```

A reader who reaches for the manual section first will not naturally look for the master equation list inside the multiband section. The promotion is a one-line edit.

**3. Forward references and a typo in entry 8.** In the "Used in" column of Table~\ref{tab:keyresults}, entry 8 reads "Protocol B (intermediate)". For consistency with entry 9, which says "SOC spectroscopy", and to make the link more concrete, consider:

```latex
8 & Intermediate-SOC, $s$-wave & ... & ... & Protocol B (Sec.~\ref{sec:protocolB})\\
```

The same applies to entries 5, 6, 7 ("Protocol B (ellipsoid)", "Protocol B (simplex)", "Sec.~\ref{sec:K2Cr3As3-bandtension}"). Entries that reference protocols by letter, with optional parenthetical tag, are fine as-is; the only real entry that points to a section rather than a protocol is entry 7, which is good. Just standardize the parenthetical: "(ellipsoid)" vs "(simplex)" vs "(intermediate)" — these are not quite parallel constructions. Consider:

- Entry 5: `Protocol B`
- Entry 6: `Protocol B (Eq.~\eqref{eq:trace-from-ellipsoid})`
- Entry 8: `Protocol B (Sec.~\ref{sec:intermediate})`

Or simply drop the parentheticals and let all three say "Protocol B".

**4. Eq.~\eqref{eq:T1-K2Cr3As3} — label on wrong line.** In the K₂Cr₃As₃ §,

```latex
\begin{align}
    \mathbf{H}\parallel\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{a}+\pi_{b})\chi_{N}\approx 0,\\
    \mathbf{H}\perp\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{b}+\pi_{c})\chi_{N}\approx\chi_{N}.
    \label{eq:T1-K2Cr3As3}
\end{align}
```

The `\label{eq:T1-K2Cr3As3}` is attached to the second line. `\eqref{eq:T1-K2Cr3As3}` will refer to the second equation's number, which is fine if you only need to point to "the $\mathbf{H}\perp\hat c$ case", but the surrounding text says "Applying ... to Eq.~\eqref{eq:K2Cr3As3-pi}" without ever citing this equation pair. If you want the pair as a single citable entity, use `subequations`:

```latex
\begin{subequations}\label{eq:T1-K2Cr3As3}
\begin{align}
    \mathbf{H}\parallel\hat c:&\quad ... \label{eq:T1-K2Cr3As3-par}\\
    \mathbf{H}\perp\hat c:&\quad ... \label{eq:T1-K2Cr3As3-perp}
\end{align}
\end{subequations}
```

Or if the label is unused, just drop it. Currently it sits in a slightly orphan state.

**5. Trivial: bridge paragraph at the end of the key-results subsection.** The paragraph that opens with "The preceding theory sections produced four kinds of input..." would more naturally be the opening paragraph of §\ref{sec:ellipsoid} than the closing paragraph of the keyresults subsection (or, if you adopt patch 2 above, of the new §\ref{sec:keyresults} section). It is a bridge into the experimental side, so it belongs at the head of that side.

## What I checked and confirmed is fine

- Figures in both appendices are now proper `figure[tb]` environments with caption inside the float — the manual-counter hack is gone. Good.
- `\centering` rather than `\begin{center}` inside both appendix figures. Good.
- Smart quotes ` `` ` and ` '' ` in the Table~\ref{tab:protocols} caption. Good.
- `\usepackage{bm}` appears once. Good.
- `floatfix` option is removed. Good (slightly safer in revtex4-2).
- All widetext equations are inside `\begin{widetext}...\end{widetext}`. Good.

## Two small physics-presentation notes

(a) In Sec.~\ref{sec:K2Cr3As3-bandtension}, the sentence after the bullet list:

> "...the tension captured in Eq.~\eqref{eq:K2Cr3As3-pred-SOC} makes this contradiction quantitative."

This is fine but the antecedent of "this contradiction" is slightly ambiguous (the contradiction between DFT $\gamma$-band isotropy and mechanism (b), or between Eq.~\eqref{eq:K2Cr3As3-pred-SOC} and Eq.~\eqref{eq:K2Cr3As3-pi}?). A small rewording:

> "...the tension captured in Eq.~\eqref{eq:K2Cr3As3-pred-SOC} \emph{quantifies} this contradiction: the SOC-driven mechanism (b), built on the DFT-indicated $\gamma$-band isotropy, would place the data point at $(0.25, 0.25, 0.50)$ rather than at the observed $(0, 0, 1)$."

(b) The closing sentence of the verdict:

> "...the specific anisotropic identities and the pocket/site bounds used later require rederivation."

is the only place where you use "later" in a way that points backward (the pocket/site bounds appear earlier in the paper, not later). Replace "used later" with "developed above" or "of Sec.~\ref{sec:multiband}".

## Minimal patch bundle (highest impact)

If you want to ship v16 with the smallest set of edits that materially improves the paper:

1. Period → comma in Eq.~\eqref{eq:K-intermediate}.
2. Promote `\subsection{Summary of key identities...}` to `\section{Reference table of key identities}`, moved to sit between §\ref{sec:multiband} and §\ref{sec:ellipsoid}, with the bridge paragraph moved to open §\ref{sec:ellipsoid}.
3. Drop the unused `\label{eq:T1-K2Cr3As3}` (or wrap the align in `subequations`).
4. Fix "used later" → "developed above" in the K₂Cr₃As₃ verdict subsection.

Each is a one- or two-line edit. None changes physics content. With these four in place I'd say the paper is ready for a coauthor pass.

Want me to produce these as concrete patch blocks like before?

---
## 🧑‍💻 User

Yes, please give me the whole paragraphs.

---
## 🤖 Assistant

Here are the four patches as complete drop-in paragraphs.

## Patch 1 — Eq.~\eqref{eq:K-intermediate} period → comma

Find this block in §\ref{sec:ellipsoid} (subsection "Intermediate-SOC regime: ellipsoid contraction"):

```latex
	\subsection{Intermediate-SOC regime: ellipsoid contraction}
	
	In the intermediate-SOC $s$-wave case of Eq.~\eqref{eq:chi-explicit}, the scalar-hyperfine Knight shift reads
	\begin{widetext}
	\begin{equation}
		\frac{K(\hat{\mathbf{H}},0)}{K_{N}}=\big\langle F_{s}(\lambda_{\mathbf{k}})\big[1-(\hat{\mathbf{H}}\cdot\hat n_{\mathbf{k}})^{2}\big]\big\rangle_{\rm FS}
		\equiv S(\lambda)-\hat{\mathbf{H}}\cdot\Pi^{\rm eff}(\lambda)\cdot\hat{\mathbf{H}}.
		\label{eq:K-intermediate}
	\end{equation}
	\end{widetext}
	with $S(\lambda)\equiv\langle F_{s}(\lambda_{\mathbf{k}})\rangle_{\rm FS}$ and
```

Replace with (period at the end of the equation becomes a comma):

```latex
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
```

## Patch 2 — Promote keyresults to a top-level section and move the bridge paragraph

This is two coordinated edits: remove the subsection from §\ref{sec:multiband} and create a new top-level §\ref{sec:keyresults} between §\ref{sec:multiband} and §\ref{sec:ellipsoid}. The bridge paragraph that currently follows the table moves to the head of §\ref{sec:ellipsoid}.

**Step 2a.** In §\ref{sec:multiband}, delete the following block in its entirety (the subsection wrapper, the intro paragraph, the table, and the bridge paragraph that follows the table):

```latex
	\subsection{Summary of key identities and inequalities}
	\label{sec:keyresults}
	
	Table~\ref{tab:keyresults} collects the central identities and inequalities of the theoretical part for reference in the experimental sections that follow. Each entry is keyed to the protocol that deploys it.
	
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
			2 & Universal $T=0$ bound & $\chi_{O}(0)\le\tfrac{2}{3}\,\chi_{O}^{N}$ & 3D isotropic FS, any $O$ & Eq.~\eqref{eq:universal-23}\\
			3 & Isotropic trace bound & $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ & 3D isotropic FS & Protocol A\\
			4 & Site-resolved bound & $\mathrm{Tr}\,K^{(\mathbf{R})}(0)/\mathrm{Tr}\,K^{(\mathbf{R})}(T_{c})\le 2/3$ & any nucleus $\mathbf{R}$, isotropic FS & Protocol E\\
			5 & Strong-locking identity & $\chi_{\mu\nu}(0)/\chi_{N}=\delta_{\mu\nu}-\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ & $|\mathbf{g}|/\Delta\to\infty$ or unitary triplet & Protocol B (ellipsoid)\\
			6 & Trace from ellipsoid & $\sum_{i}K_{i}(0)=2K_{N}$ & strong locking, any FS/SOC & Protocol B (simplex)\\
			7 & Helicity-diagonal $T=0$ & $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ & parity mixture with $\Delta_{\perp}=0$, fully gapped & Sec.~\ref{sec:K2Cr3As3-bandtension}\\
			8 & Intermediate-SOC, $s$-wave & $\chi_{\mu\nu}(0)/\chi_{N}=\langle F_{s}(\lambda_{\mathbf{k}})[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\rangle_{\rm FS}$ & $\mathbf{H}=0$, $s$-wave, any SOC & Protocol B (intermediate)\\
			9 & $F_{s}$ closed form & $F_{s}(\lambda)=1-\sinh^{-1}\!\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ & same as \#8 & SOC spectroscopy\\
			10 & Finite-$\mathbf{H}$ strong locking & $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]+O(\Delta^{2}/b_{\min}^{2})$ & $b_{\min}(\mathbf{H})\gg\Delta$ & Protocol C\\
			11 & Zero-field stability & $\Pi_{\mu\nu}(\mathbf{H})=\Pi_{\mu\nu}(0)+O(h^{2}/\lambda^{2})$ & $\mu_{B}H\ll|\mathbf{g}_{\mathbf{k}}|$ on FS & Protocol C (low field)\\
			12 & Spin FGT sum rule & $\tfrac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}[\mathrm{Im}\chi^{N}-\mathrm{Im}\chi^{SC}]=\chi_{N}\pi_{\mu}$ & strong locking, $\mathbf{q}=0$ & Protocol D\\
			13 & $1/T_{1}$ heuristic bound & $\int_{0}^{T_{c}}\!\frac{dT}{T}[(T_{1}^{N})^{-1}-(T_{1}^{SC})^{-1}]\lesssim\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\pi_{\mu}$ & $\mathbf{q}\approx 0$ dominant & Protocol D\\
			14 & Multiband decomposition & $\chi_{\mu\nu}(0)=\sum_{i}\chi_{N}^{(i)}[\delta_{\mu\nu}-\Pi^{(i)}_{\mu\nu}]$ & orbital-diagonal pairing & Protocol F\\
			15 & Multiband trace bound & $\mathrm{Tr}\,\chi(0)\le(2/3)\mathrm{Tr}\,\chi(T_{c})$ & 3D isotropic FS, any pairing & survives interband mixing\\
			\hline\hline
		\end{tabular}
	\end{table*}
	
		The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem of Sec.~\ref{sec:ellipsoid}. Next, Sec.~\ref{sec:protocols} packages the remaining ingredients as successive layers of inference: start from the trace bound when only limited data exist, upgrade to the full ellipsoid when rotation data are available, then add finite field, $1/T_1$, site resolution, and pocket decomposition only when needed. Section~\ref{sec:K2Cr3As3} finally applies that manual to K$_{2}$Cr$_{3}$As$_{3}$ in the same order.
```

**Step 2b.** Between the end of §\ref{sec:multiband} and the start of §\ref{sec:ellipsoid}, insert this new top-level section:

```latex
	\section{Reference table of key identities}
	\label{sec:keyresults}
	
	Before turning to the experimental manual we collect the central identities and inequalities derived above. Each entry in Table~\ref{tab:keyresults} is keyed by domain of validity and to the protocol of Sec.~\ref{sec:protocols} that deploys it; readers entering the manuscript at the manual can use this table as a stand-alone reference.
	
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
			1 & Plancherel identity & $\sum_{s_{1}s_{2}}\!\big[|M^{s_{1}s_{2}}_{

---
## 🧑‍💻 User

continue from where it is cut off

---
## 🤖 Assistant

Continuing Patch 2 from where it was cut off:

```latex
	\section{Reference table of key identities}
	\label{sec:keyresults}
	
	Before turning to the experimental manual we collect the central identities and inequalities derived above. Each entry in Table~\ref{tab:keyresults} is keyed by domain of validity and to the protocol of Sec.~\ref{sec:protocols} that deploys it; readers entering the manuscript at the manual can use this table as a stand-alone reference.
	
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
			2 & Universal $T=0$ bound & $\chi_{O}(0)\le\tfrac{2}{3}\,\chi_{O}^{N}$ & 3D isotropic FS, any $O$ & Eq.~\eqref{eq:universal-23}\\
			3 & Isotropic trace bound & $\mathrm{Tr}\,\chi(0)\le 2\chi_{N}$ & 3D isotropic FS & Protocol A\\
			4 & Site-resolved bound & $\mathrm{Tr}\,K^{(\mathbf{R})}(0)/\mathrm{Tr}\,K^{(\mathbf{R})}(T_{c})\le 2/3$ & any nucleus $\mathbf{R}$, isotropic FS & Protocol E\\
			5 & Strong-locking identity & $\chi_{\mu\nu}(0)/\chi_{N}=\delta_{\mu\nu}-\langle\hat n_{\mu}\hat n_{\nu}\rangle_{\rm FS}$ & $|\mathbf{g}|/\Delta\to\infty$ or unitary triplet & Protocol B\\
			6 & Trace from ellipsoid & $\sum_{i}K_{i}(0)=2K_{N}$ & strong locking, any FS/SOC & Protocol B\\
			7 & Helicity-diagonal $T=0$ & $\chi_{\mu\nu}(0)=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}]$ & parity mixture with $\Delta_{\perp}=0$, fully gapped & Sec.~\ref{sec:K2Cr3As3-bandtension}\\
			8 & Intermediate-SOC, $s$-wave & $\chi_{\mu\nu}(0)/\chi_{N}=\langle F_{s}(\lambda_{\mathbf{k}})[\delta_{\mu\nu}-\hat n_{\mu}\hat n_{\nu}]\rangle_{\rm FS}$ & $\mathbf{H}=0$, $s$-wave, any SOC & Protocol B\\
			9 & $F_{s}$ closed form & $F_{s}(\lambda)=1-\sinh^{-1}\!\lambda/[\lambda\sqrt{1+\lambda^{2}}]$ & same as \#8 & SOC spectroscopy\\
			10 & Finite-$\mathbf{H}$ strong locking & $\chi_{\mu\nu}(0,\mathbf{H})=\chi_{N}[\delta_{\mu\nu}-\Pi_{\mu\nu}(\mathbf{H})]+O(\Delta^{2}/b_{\min}^{2})$ & $b_{\min}(\mathbf{H})\gg\Delta$ & Protocol C\\
			11 & Zero-field stability & $\Pi_{\mu\nu}(\mathbf{H})=\Pi_{\mu\nu}(0)+O(h^{2}/\lambda^{2})$ & $\mu_{B}H\ll|\mathbf{g}_{\mathbf{k}}|$ on FS & Protocol C\\
			12 & Spin FGT sum rule & $\tfrac{2}{\pi}\int_{0}^{\infty}\!\frac{d\omega}{\omega}[\mathrm{Im}\chi^{N}-\mathrm{Im}\chi^{SC}]=\chi_{N}\pi_{\mu}$ & strong locking, $\mathbf{q}=0$ & Protocol D\\
			13 & $1/T_{1}$ heuristic bound & $\int_{0}^{T_{c}}\!\frac{dT}{T}[(T_{1}^{N})^{-1}-(T_{1}^{SC})^{-1}]\lesssim\gamma_{n}^{2}k_{B}\langle|A_{\rm hf}|^{2}\rangle\chi_{N}\pi_{\mu}$ & $\mathbf{q}\approx 0$ dominant & Protocol D\\
			14 & Multiband decomposition & $\chi_{\mu\nu}(0)=\sum_{i}\chi_{N}^{(i)}[\delta_{\mu\nu}-\Pi^{(i)}_{\mu\nu}]$ & orbital-diagonal pairing & Protocol F\\
			15 & Multiband trace bound & $\mathrm{Tr}\,\chi(0)\le(2/3)\mathrm{Tr}\,\chi(T_{c})$ & 3D isotropic FS, any pairing & survives interband mixing\\
			\hline\hline
		\end{tabular}
	\end{table*}
```

(Compared to v15: the parentheticals in the "Used in" column for entries 5, 6, 8, 11 are standardized — the now-redundant tags `(ellipsoid)`, `(simplex)`, `(intermediate)`, `(low field)` are dropped, since the table caption and the protocols section already make the role clear.)

**Step 2c.** At the start of §\ref{sec:ellipsoid}, insert the moved bridge paragraph just before the existing first paragraph:

Find this current opening of §\ref{sec:ellipsoid}:

```latex
	\section[Core Diagnostic]{Core diagnostic: Knight-shift ellipsoid}
	\label{sec:ellipsoid}
	
	This section is the conceptual core of the measurement side of the paper. It turns Eq.~\eqref{eq:unified} into a directly measurable geometric object and then classifies the allowed shapes before the protocol section operationalizes the construction.
```

Replace with:

```latex
	\section[Core Diagnostic]{Core diagnostic: Knight-shift ellipsoid}
	\label{sec:ellipsoid}
	
	The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem of the present section. Next, Sec.~\ref{sec:protocols} packages the remaining ingredients as successive layers of inference: start from the trace bound when only limited data exist, upgrade to the full ellipsoid when rotation data are available, then add finite field, $1/T_1$, site resolution, and pocket decomposition only when needed. Section~\ref{sec:K2Cr3As3} finally applies that manual to K$_{2}$Cr$_{3}$As$_{3}$ in the same order.
	
	This section is the conceptual core of the measurement side of the paper. It turns Eq.~\eqref{eq:unified} into a directly measurable geometric object and then classifies the allowed shapes before the protocol section operationalizes the construction.
```

(Note the small edit: "this is the ellipsoid theorem of Sec.~\ref{sec:ellipsoid}" → "this is the ellipsoid theorem of the present section", since the bridge now sits inside §\ref{sec:ellipsoid} itself.)

## Patch 3 — Drop the dangling label on Eq.~\eqref{eq:T1-K2Cr3As3}

In §\ref{sec:K2Cr3As3-T1}, find:

```latex
	\begin{align}
		\mathbf{H}\parallel\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{a}+\pi_{b})\chi_{N}\approx 0,\\
		\mathbf{H}\perp\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{b}+\pi_{c})\chi_{N}\approx\chi_{N}.
		\label{eq:T1-K2Cr3As3}
	\end{align}
```

Replace with (label simply removed; the equation pair is not cited anywhere in the text):

```latex
	\begin{align}
		\mathbf{H}\parallel\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{a}+\pi_{b})\chi_{N}\approx 0,\\
		\mathbf{H}\perp\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{b}+\pi_{c})\chi_{N}\approx\chi_{N}.
	\end{align}
```

If you prefer to keep a label for future referencing, instead use `subequations` to attach it to the pair:

```latex
	\begin{subequations}\label{eq:T1-K2Cr3As3}
	\begin{align}
		\mathbf{H}\parallel\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{a}+\pi_{b})\chi_{N}\approx 0,\\
		\mathbf{H}\perp\hat c:&\quad \text{$\mathbf{q}=0$ bound}\ \propto\ (\pi_{b}+\pi_{c})\chi_{N}\approx\chi_{N}.
	\end{align}
	\end{subequations}
```

## Patch 4 — Fix "used later" in K₂Cr₃As₃ verdict

In §\ref{sec:K2Cr3As3-verdict}, find the sentence ending with "used later require rederivation":

```latex
		We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline;

---
## 🧑‍💻 User

This is the revised version. Please go through it.

---
## 🤖 Assistant

I went through the new v15. Most of the patches landed cleanly — the comma in Eq.~\eqref{eq:K-intermediate}, the promoted `\section{Reference table of key identities}`, the moved bridge paragraph at the head of §\ref{sec:ellipsoid}, the `subequations` wrapper for the K₂Cr₃As₃ relaxation pair, the smart quotes in Table~\ref{tab:protocols} caption, the proper float environments in both appendices. Good.

There is one place where the previous edit was applied too aggressively, plus one small leftover.

## Issue 1 (must fix) — Truncated paragraph in §\ref{sec:K2Cr3As3-verdict}

Look at this paragraph as it currently stands:

```latex
	We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline;
	
	A targeted follow-up is an As1-vs-As2 site-resolved test (Protocol~E): ...
```

The sentence ends mid-clause with a semicolon — the "Baseline theoretical inference" definition is truncated, and the closing material from the previous version ("the pure OSP limit with a common $\mathbf{d}$ vector is the simplest realization, but a helicity-diagonal parity admixture is not excluded by the $T=0$ ellipsoid alone. A definitive microscopic selection in the presence of strong inter-band pairing requires a multi-orbital BdG analysis...") was lost when patch 4 was applied. Most likely this happened because patch 4 was started but the original sentence ending was overwritten rather than just edited.

The fix is to restore the rest of the paragraph. Replace the current paragraph

```latex
	We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline;
```

with the full version:

```latex
	We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline; the pure OSP limit with a common $\mathbf{d}$ vector is the simplest realization, but a helicity-diagonal parity admixture is not excluded by the $T=0$ ellipsoid alone. A definitive microscopic selection in the presence of strong inter-band pairing requires a multi-orbital BdG analysis---the Plancherel identity Eq.~\eqref{eq:general-sum-rule} survives that extension unchanged, but the specific anisotropic identities and the pocket/site bounds developed above require rederivation.
```

(Compared to v14 this also incorporates Patch 4: "used later" → "developed above".)

## Issue 2 (minor) — Dangling forward reference inside §\ref{sec:multiband}

In §\ref{sec:multiband}, the scope subsection ends with:

```latex
A dedicated multi-orbital derivation is required, however, before importing the anisotropic simplex interpretation of Sec.~\ref{sec:ellipsoid}, or the normalized site/pocket bounds used later, to genuine inter-band pairing.
```

This still says "used later" — for parallelism with the K₂Cr₃As₃ verdict fix above, change to "used in the protocols below" or "deployed in Sec.~\ref{sec:protocols}". Suggested:

```latex
A dedicated multi-orbital derivation is required, however, before importing the anisotropic simplex interpretation of Sec.~\ref{sec:ellipsoid}, or the normalized site/pocket bounds deployed in Sec.~\ref{sec:protocols}, to genuine inter-band pairing.
```

## Issue 3 (very minor) — One leftover forward "used later" in §\ref{sec:intro}

In the second paragraph of §\ref{sec:intro}:

```latex
... and Sec.~\ref{sec:multiband} isolates the decoupled multiband baseline used later in the measurement analysis.
```

Here "used later" is fine because it refers forward; the sentence reads naturally as a paragraph that previews the structure of the paper. No action needed unless you want all "used later" phrasings out of the manuscript for consistency.

## Issue 4 (very minor) — Forward reference text in §\ref{sec:ellipsoid}'s opening bridge

The bridge paragraph now opening §\ref{sec:ellipsoid} reads:

```latex
The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem of the present section.
```

The "of the present section" reads slightly awkwardly because the bridge paragraph now opens the section it points to. Cleaner alternatives:

> "...this is the ellipsoid theorem developed below."

or simply

> "...this is the ellipsoid theorem of this section."

Either is fine; the "present section" phrasing came from when I converted "of Sec.~\ref{sec:ellipsoid}" to refer to the same section.

## Spot-checks that pass

- The promoted `\section{Reference table of key identities}` sits in the right place, between §\ref{sec:multiband} and §\ref{sec:ellipsoid}, with the `table*` inside it. Good.
- `\label{sec:keyresults}` is now attached to the new section rather than a subsection. Good.
- The "Used in" column entries are standardized (no more "(ellipsoid)", "(simplex)", etc.). Good.
- `\begin{subequations}\label{eq:T1-K2Cr3As3}` wrapping in §\ref{sec:K2Cr3As3-T1} is correctly closed and the inner align has no orphan label. Good.
- All `\begin{widetext}` blocks are properly closed. Good.
- Both appendix figures use real `figure[tb]` floats with `\caption{}` and `\label{}` inside the float, no `\refstepcounter` hack. Good.
- The smart quotes in Table~\ref{tab:protocols} caption render correctly. Good.

## Summary

The only real issue is the truncated verdict paragraph in §\ref{sec:K2Cr3As3-verdict}. Items 2–4 are stylistic. After fixing item 1, I would consider the manuscript ready to circulate to coauthors.

If you would like, I can produce the full corrected paragraph as a single drop-in replacement, or roll items 2–4 into the same minimal patch.

---
## 🧑‍💻 User

pls

---
## 🤖 Assistant

Here is the consolidated patch addressing all four items.

## Patch — replace four passages in v15

### Patch item 1 — restore the truncated verdict paragraph

In §\ref{sec:K2Cr3As3-verdict}, find this truncated paragraph:

```latex
	We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline;
```

Replace with the complete version:

```latex
	We distinguish two levels of conclusion. \emph{Robust experimental statement}: the Knight-shift tensor sits at the $\hat c$ vertex, and any acceptable microscopic theory must reproduce that near-vertex ellipsoid. \emph{Baseline theoretical inference}: within the orbital-diagonal framework of Eq.~\eqref{eq:a2cr3as3-pred}, the data favor a common-$\hat c$ locking interpretation over the independent-pocket SOC-texture baseline; the pure OSP limit with a common $\mathbf{d}$ vector is the simplest realization, but a helicity-diagonal parity admixture is not excluded by the $T=0$ ellipsoid alone. A definitive microscopic selection in the presence of strong inter-band pairing requires a multi-orbital BdG analysis---the Plancherel identity Eq.~\eqref{eq:general-sum-rule} survives that extension unchanged, but the specific anisotropic identities and the pocket/site bounds developed above require rederivation.
```

### Patch item 2 — remove "used later" in §\ref{sec:multiband} scope subsection

In §\ref{sec:multiband}, the subsection "Scope: inter-band pairing as deviation from baseline", find:

```latex
	Equation~\eqref{eq:multiband-id} is exact for orbital-diagonal pairing and is a baseline otherwise: deviations diagnose the inter-band structure. The trace inequality Eq.~\eqref{eq:multiband-bound}, in contrast, follows directly from the pointwise Plancherel bound $\sum|M_{pp,O}|^{2}\le\mathrm{Tr}_{s}(O^{2})$ and the isotropic-FS geometric factor $\langle\cos^{2}\theta\rangle=1/3$; it therefore survives inter-band pairing on a 3D isotropic FS. The Plancherel identity Eq.~\eqref{eq:general-sum-rule} itself is independent of the orbital-diagonal assumption. A dedicated multi-orbital derivation is required, however, before importing the anisotropic simplex interpretation of Sec.~\ref{sec:ellipsoid}, or the normalized site/pocket bounds used later, to genuine inter-band pairing.
```

Replace with:

```latex
	Equation~\eqref{eq:multiband-id} is exact for orbital-diagonal pairing and is a baseline otherwise: deviations diagnose the inter-band structure. The trace inequality Eq.~\eqref{eq:multiband-bound}, in contrast, follows directly from the pointwise Plancherel bound $\sum|M_{pp,O}|^{2}\le\mathrm{Tr}_{s}(O^{2})$ and the isotropic-FS geometric factor $\langle\cos^{2}\theta\rangle=1/3$; it therefore survives inter-band pairing on a 3D isotropic FS. The Plancherel identity Eq.~\eqref{eq:general-sum-rule} itself is independent of the orbital-diagonal assumption. A dedicated multi-orbital derivation is required, however, before importing the anisotropic simplex interpretation of Sec.~\ref{sec:ellipsoid}, or the normalized site/pocket bounds deployed in Sec.~\ref{sec:protocols}, to genuine inter-band pairing.
```

### Patch item 3 — clean up "of the present section" in the §\ref{sec:ellipsoid} bridge

In §\ref{sec:ellipsoid}, find the opening bridge paragraph:

```latex
	The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem of the present section. Next, Sec.~\ref{sec:protocols} packages the remaining ingredients as successive layers of inference: start from the trace bound when only limited data exist, upgrade to the full ellipsoid when rotation data are available, then add finite field, $1/T_1$, site resolution, and pocket decomposition only when needed. Section~\ref{sec:K2Cr3As3} finally applies that manual to K$_{2}$Cr$_{3}$As$_{3}$ in the same order.
```

Replace with (one phrase change):

```latex
	The preceding theory sections produced four kinds of input: a scalar bound, a tensor geometry, controlled departures from the ideal strong-locking limit, and structural extensions to dynamics and multiple pockets. The remaining sections use them in the same order an experiment would. First, the strong-locking identity Eq.~\eqref{eq:unified}, $\chi_{\mu\nu}(0)/\chi_N=\delta_{\mu\nu}-\Pi_{\mu\nu}$, is read directly as a map from the measurable Knight-shift tensor to the projection tensor $\Pi$; this is the ellipsoid theorem developed below. Next, Sec.~\ref{sec:protocols} packages the remaining ingredients as successive layers of inference: start from the trace bound when only limited data exist, upgrade to the full ellipsoid when rotation data are available, then add finite field, $1/T_1$, site resolution, and pocket decomposition only when needed. Section~\ref{sec:K2Cr3As3} finally applies that manual to K$_{2}$Cr$_{3}$As$_{3}$ in the same order.
```

### Patch item 4 (optional) — "used later" in introduction

If you want to remove the last "used later" phrasing for full consistency, in §\ref{sec:intro} find:

```latex
... and Sec.~\ref{sec:multiband} isolates the decoupled multiband baseline used later in the measurement analysis.
```

Replace with:

```latex
... and Sec.~\ref{sec:multiband} isolates the decoupled multiband baseline used in the measurement analysis of Sec.~\ref{sec:protocols} and the worked example of Sec.~\ref{sec:K2Cr3As3}.
```

This one is genuinely optional — "used later" reads fine in a paragraph that is previewing the structure of the paper.

---

After applying patch items 1, 2, and 3, the manuscript is internally consistent and ready to circulate. Item 4 is cosmetic.
