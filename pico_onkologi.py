"""Generator sederhana ide PICO onkologi radiasi.

Jalankan:
    python pico_onkologi.py
"""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class PicoStudy:
    """Representasi 1 ide studi berbasis PICO."""

    title: str
    population: str
    intervention: str
    comparison: str
    outcomes: List[str]

    def to_markdown(self, index: int) -> str:
        outcome_text = ", ".join(self.outcomes)
        return (
            f"{index}) **{self.title}**\n"
            f"- **P:** {self.population}\n"
            f"- **I:** {self.intervention}\n"
            f"- **C:** {self.comparison}\n"
            f"- **O:** {outcome_text}\n"
        )


def default_ideas() -> List[PicoStudy]:
    """Daftar ide dasar yang bisa dipakai ulang/diadaptasi."""

    return [
        PicoStudy(
            title="AutoContour-One",
            population="Pasien H&N/prostat/paru kandidat IMRT/VMAT",
            intervention="AI auto-contouring target + OAR",
            comparison="Contouring manual",
            outcomes=[
                "Waktu contouring",
                "Variasi antar-dokter",
                "Kualitas DVH",
                "Jumlah revisi plan",
            ],
        ),
        PicoStudy(
            title="Dose-Drift Detector",
            population="Pasien RT fraksinasi panjang (H&N/cervix)",
            intervention="AI deteksi perubahan anatomi harian dari CBCT",
            comparison="Evaluasi manual periodik",
            outcomes=[
                "Overdosis OAR",
                "Cakupan target (D95)",
                "Ketepatan waktu replanning",
                "Toksisitas",
            ],
        ),
        PicoStudy(
            title="PneumoShield",
            population="Pasien RT toraks (NSCLC)",
            intervention="AI radiomics CT + dose-volume",
            comparison="Constraint DVH konvensional (V20/MLD)",
            outcomes=[
                "Pneumonitis grade ≥2",
                "AUC/kalibrasi model",
                "Hospitalisasi",
            ],
        ),
    ]


def render_markdown(studies: List[PicoStudy]) -> str:
    """Render semua studi ke markdown terstruktur."""

    header = "# Ide PICO Onkologi Radiasi\n\n"
    body = "\n".join(study.to_markdown(i + 1) for i, study in enumerate(studies))
    return header + body


def main() -> None:
    print(render_markdown(default_ideas()))


if __name__ == "__main__":
    main()
