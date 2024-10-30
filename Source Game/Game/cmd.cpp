//Add 
#ifdef ENABLE_EXP_TEXT
ACMD(do_exp_text);
#endif

//Add before NULL
#ifdef ENABLE_EXP_TEXT
{ "do_exp_text", CmdToggleExpText, 0, POS_DEAD, GM_PLAYER },
#endif
