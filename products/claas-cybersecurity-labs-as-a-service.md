---
type: product
id: claas-cybersecurity-labs-as-a-service
title: CLaaS (Cybersecurity Labs-as-a-Service)
description: CLaaS is an AWS-based, browser-accessible cybersecurity lab platform developed for university cybersecurity courses, with an integrated OCR-to-LLM assistant for simplifying lab instructions.
product_kind: software
status: draft
generated:
  by: "process:settle-candidates"
  at: 2026-10-10
---

# CLaaS (Cybersecurity Labs-as-a-Service)

> **Product or Programme** · [All products and programmes](index.md)
> **Evidence** · 2 claims (2 for) · 1 study (1 design), `q2` · 0 of 1 report an effect size · 2 claims rest on one study

## Description
CLaaS is an AWS-based, browser-accessible cybersecurity lab platform developed for university cybersecurity courses, with an integrated OCR-to-LLM assistant for simplifying lab instructions.

## Components
<!-- A programme's own frameworks, tools, indicators and instruments, as its sources describe them -->
- **CLaaS platform with integrated OCR-to-LLM instructional assistant**: CLaaS (Cybersecurity Labs-as-a-Service) is an AWS cloud-based platform delivering browser-accessible cybersecurity labs via EC2 virtual machines, supporting tasks such as DDoS attacks, buffer overflows, packet sniffing, and ransomware attacks. This paper extends it with an "Instruction Simplification" button that captures the current slide as an image, extracts text with Tesseract OCR, and sends the raw text with a crafted prompt to an LLM (gpt-4) via API to generate a simplified, zero-shot explanation delivered in the CLaaS interface. Students rate the output on a 1-10 feedback scale stored for later analysis and prompt personalization. (Patel et al. (2025))

### Claims
- [Students rate LLM-generated simplified instructions positively, averaging 7.83 on a 1-10 usefulness scale across 42 ratings in a live cybersecurity course](../claims/student-feedback-7-83-ocr-llm-instructions.md) [+M]
- [Multimodal LLMs outperform the OCR-based pipeline on visually dense slides, while the OCR pipeline produces comparable instruction on text-centric slides](../claims/multimodal-vs-ocr-pipeline-slide-type-comparison.md) [+M]

## Related Products and Programmes
-

## Key Sources
- Patel, K., Lin, Y.-Z., Raul, G., Shih, B. P.-J., Redondo, M. W., Latibari, B. S., Pacheco, J., Salehi, S., & Satam, P. (2025). Integrating Generative AI into Cybersecurity Education: A Study of OCR and Multimodal LLM-assisted Instruction. arXiv. https://arxiv.org/abs/2509.02998
