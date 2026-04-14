from src.pipeline import eval_case


def test_eval_case_real_case_file():
    row = eval_case("data/case_files/computing/tcp_ip_1981.json")

    assert row["id"] == "anima:computing:tcp_ip_1981"
    assert row["domain"] == "computing"
    assert isinstance(row["mdl_delta"], float)
    assert isinstance(row["network_rupture"], float)
    assert 0.0 <= row["L_star"] <= 1.0
