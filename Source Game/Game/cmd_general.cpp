//Add in the end
#ifdef ENABLE_EXP_TEXT
ACMD(CmdToggleExpText)
{
    ch->SetShowExpText(!ch->IsShowExpText());
    if (ch->IsShowExpText())
    {
        ch->ChatPacket(CHAT_TYPE_INFO, "Experience text is now shown.");
    }
    else
    {
        ch->ChatPacket(CHAT_TYPE_INFO, "Experience text is now hidden.");
    }
}
#endif
