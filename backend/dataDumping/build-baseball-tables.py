import sqlite3

def create_schema(connection):
    """
    Creates tables for the baseball database based on comprehensive schema definitions.
    """
    cursor = connection.cursor()

    # Create Statcast Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS statcast (
        pitch_type TEXT,
        game_date TEXT,
        release_speed REAL,
        release_pos_x REAL,
        release_pos_z REAL,
        player_name TEXT,
        batter INTEGER,
        pitcher INTEGER,
        events TEXT,
        description TEXT,
        spin_dir REAL,
        spin_rate_deprecated REAL,
        break_angle_deprecated REAL,
        break_length_deprecated REAL,
        zone INTEGER,
        des TEXT,
        game_type TEXT,
        stand TEXT,
        p_throws TEXT,
        home_team TEXT,
        away_team TEXT,
        type TEXT,
        hit_location INTEGER,
        bb_type TEXT,
        balls INTEGER,
        strikes INTEGER,
        game_year INTEGER,
        pfx_x REAL,
        pfx_z REAL,
        plate_x REAL,
        plate_z REAL,
        on_3b INTEGER,
        on_2b INTEGER,
        on_1b INTEGER,
        outs_when_up INTEGER,
        inning INTEGER,
        inning_topbot TEXT,
        hc_x REAL,
        hc_y REAL,
        tfs_deprecated TEXT,
        tfs_zulu_deprecated TEXT,
        umpire TEXT,
        sv_id TEXT,
        vx0 REAL,
        vy0 REAL,
        vz0 REAL,
        ax REAL,
        ay REAL,
        az REAL,
        sz_top REAL,
        sz_bot REAL,
        hit_distance_sc REAL,
        launch_speed REAL,
        launch_angle REAL,
        effective_speed REAL,
        release_spin_rate REAL,
        release_extension REAL,
        game_pk INTEGER,
        fielder_2 INTEGER,
        fielder_3 INTEGER,
        fielder_4 INTEGER,
        fielder_5 INTEGER,
        fielder_6 INTEGER,
        fielder_7 INTEGER,
        fielder_8 INTEGER,
        fielder_9 INTEGER,
        release_pos_y REAL,
        estimated_ba_using_speedangle REAL,
        estimated_woba_using_speedangle REAL,
        woba_value REAL,
        woba_denom REAL,
        babip_value REAL,
        iso_value REAL,
        launch_speed_angle REAL,
        at_bat_number INTEGER,
        pitch_number INTEGER,
        pitch_name TEXT,
        home_score INTEGER,
        away_score INTEGER,
        bat_score INTEGER,
        fld_score INTEGER,
        post_away_score INTEGER,
        post_home_score INTEGER,
        post_bat_score INTEGER,
        post_fld_score INTEGER,
        if_fielding_alignment TEXT,
        of_fielding_alignment TEXT,
        spin_axis REAL,
        delta_home_win_exp REAL,
        delta_run_exp REAL,
        bat_speed REAL,
        swing_length REAL,
        estimated_slg_using_speedangle REAL,
        delta_pitcher_run_exp REAL,
        hyper_speed REAL,
        home_score_diff INTEGER,
        bat_score_diff INTEGER,
        home_win_exp REAL,
        bat_win_exp REAL,
        age_pit REAL,
        age_bat REAL,
        api_break_z_with_gravity REAL,
        api_break_x_arm REAL,
        api_break_x_batter_in REAL,
        arm_angle REAL
    );
    ''')

    # Create Fielding Stats Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS fielding_stats (
        IDfg TEXT,
        Season INTEGER,
        Name TEXT,
        Team TEXT,
        Pos TEXT,
        G INTEGER,
        GS INTEGER,
        Inn REAL,
        PO INTEGER,
        A INTEGER,
        E INTEGER,
        FE INTEGER,
        TE INTEGER,
        DP INTEGER,
        DPS INTEGER,
        DPT INTEGER,
        DPF INTEGER,
        Scp REAL,
        SB INTEGER,
        CS INTEGER,
        PB INTEGER,
        WP INTEGER,
        FP REAL,
        TZ REAL,
        rSB REAL,
        rGDP REAL,
        rARM REAL,
        rGFP REAL,
        rPM REAL,
        DRS REAL,
        BIZ REAL,
        Plays INTEGER,
        RZR REAL,
        OOZ REAL,
        TZL REAL,
        FSR REAL,
        ARM REAL,
        DPR REAL,
        RngR REAL,
        ErrR REAL,
        UZR REAL,
        "UZR/150" REAL,
        CPP REAL,
        RPP REAL,
        Def REAL,
        FRM REAL,
        OAA REAL,
        Range REAL
    );
    ''')

    # Create Pitching Stats Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS pitching_stats (
        IDfg TEXT,
        Season INTEGER,
        Name TEXT,
        Team TEXT,
        Age INTEGER,
        W INTEGER,
        L INTEGER,
        WAR REAL,
        ERA REAL,
        G INTEGER,
        GS INTEGER,
        CG INTEGER,
        ShO INTEGER,
        SV INTEGER,
        BS INTEGER,
        IP REAL,
        TBF INTEGER,
        H INTEGER,
        R INTEGER,
        ER INTEGER,
        HR INTEGER,
        BB INTEGER,
        IBB INTEGER,
        HBP INTEGER,
        WP INTEGER,
        BK INTEGER,
        SO INTEGER,
        GB INTEGER,
        FB INTEGER,
        LD INTEGER,
        IFFB INTEGER,
        Balls INTEGER,
        Strikes INTEGER,
        Pitches INTEGER,
        RS REAL,
        IFH INTEGER,
        BU INTEGER,
        BUH INTEGER,
        "K/9" REAL,
        "BB/9" REAL,
        "K/BB" REAL,
        "H/9" REAL,
        "HR/9" REAL,
        AVG REAL,
        WHIP REAL,
        BABIP REAL,
        "LOB%" REAL,
        FIP REAL,
        "GB/FB" REAL,
        "LD%" REAL,
        "GB%" REAL,
        "FB%" REAL,
        "IFFB%" REAL,
        "HR/FB" REAL,
        "IFH%" REAL,
        "BUH%" REAL,
        Starting REAL,
        "Start-IP" REAL,
        Relieving REAL,
        "Relief-IP" REAL,
        RAR REAL,
        Dollars REAL,
        tERA REAL,
        xFIP REAL
    );
    ''')

    # Create Batting Stats Table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS batting_stats (
        IDfg TEXT,
        Season INTEGER,
        Name TEXT,
        Team TEXT,
        Age INTEGER,
        G INTEGER,
        AB INTEGER,
        PA INTEGER,
        H INTEGER,
        "1B" INTEGER,
        "2B" INTEGER,
        "3B" INTEGER,
        HR INTEGER,
        R INTEGER,
        RBI INTEGER,
        BB INTEGER,
        IBB INTEGER,
        SO INTEGER,
        HBP INTEGER,
        SF INTEGER,
        SH INTEGER,
        GDP INTEGER,
        SB INTEGER,
        CS INTEGER,
        AVG REAL,
        OBP REAL,
        SLG REAL,
        OPS REAL,
        ISO REAL,
        BABIP REAL,
        WAR REAL
    );
    ''')

    # Commit changes
    connection.commit()
    print("Database schema created successfully.")

def main():
    # Connect to SQLite database
    db_name = "baseball_data.db"
    conn = sqlite3.connect(db_name)
    
    # Create the schema
    create_schema(conn)
    
    # Close connection
    conn.close()

if __name__ == "__main__":
    main()


