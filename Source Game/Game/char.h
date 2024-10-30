//Before
};

ESex GET_SEX(LPCHARACTER ch);

#endif

//Add
#ifdef ENABLE_EXP_TEXT
private:
    bool m_bShowExpText;  //Show text ON/OFF

public:
    void SetShowExpText(bool bShow) { m_bShowExpText = bShow; }
    bool IsShowExpText() const { return m_bShowExpText; }
#endif
